<?php
/*
 * NagelNEU · KI-Anbindung für den Chat-Assistenten
 * ------------------------------------------------
 * Diese Datei liegt auf DEINEM Webspace, nicht in der App. Nur hier steht der geheime Schlüssel.
 * Besucher sehen ihn nie.
 *
 * WICHTIG: GitHub Pages kann kein PHP ausführen. Diese Datei gehört auf einen Webspace mit PHP
 * (z. B. dein normaler Hoster). Und: Den Schlüssel NIE in die GitHub-Version eintragen, nur in die Kopie
 * auf deinem Webspace.
 *
 * So richtest du es ein:
 * 1. Trage unten bei API_KEY deinen Schlüssel ein (bei Anthropic beginnt er mit "sk-ant-").
 *    Noch besser: Lege ihn als Umgebungsvariable ANTHROPIC_API_KEY bei deinem Hoster an und lass das Feld leer.
 * 2. Lade die Datei auf deinen Webspace hoch, z. B. https://deine-seite.de/nagelneu/chat-proxy.php
 * 3. Liegt die App auf GitHub Pages, trage bei ALLOWED_ORIGIN deine GitHub-Adresse ein,
 *    z. B. 'https://deinname.github.io'
 * 4. Trage in der index.html bei  const CHAT_URL=''  die volle Adresse ein:
 *    const CHAT_URL='https://deine-seite.de/nagelneu/chat-proxy.php';
 *    (Liegt die App im selben Ordner auf deinem Webspace, reicht  'chat-proxy.php'.)
 *
 * Der eingebaute Assistent beantwortet weiterhin alles, was er selbst weiß. Nur Fragen, die er nicht
 * versteht, landen hier. Das spart Kosten.
 */

const API_KEY        = '';                    // ← hier eintragen oder Umgebungsvariable nutzen
const MODEL          = 'claude-haiku-5-5';    // schnell und günstig
const MAX_PER_MINUTE = 6;                     // Schutz vor Missbrauch: Anfragen pro Besucher und Minute
const ALLOWED_ORIGIN = 'https://nagelneu.github.io'; // z. B. 'https://deinname.github.io' (nötig, wenn App und PHP auf verschiedenen Adressen liegen)

header('Content-Type: application/json; charset=utf-8');
if (ALLOWED_ORIGIN !== '') { header('Access-Control-Allow-Origin: ' . ALLOWED_ORIGIN); }
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { header('Access-Control-Allow-Headers: Content-Type'); header('Access-Control-Allow-Methods: POST, OPTIONS'); exit; }
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo json_encode(['answer' => '']); exit; }

$key = API_KEY !== '' ? API_KEY : (getenv('ANTHROPIC_API_KEY') ?: '');
if ($key === '') { echo json_encode(['answer' => '']); exit; }

/* einfache Begrenzung pro IP */
$ipHash = hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? '') . 'nagelneu');
$rlFile = sys_get_temp_dir() . '/nn_rl_' . $ipHash;
$now = time();
$hits = array_filter(@json_decode(@file_get_contents($rlFile), true) ?: [], fn($t) => $t > $now - 60);
if (count($hits) >= MAX_PER_MINUTE) { echo json_encode(['answer' => '']); exit; }
$hits[] = $now; @file_put_contents($rlFile, json_encode(array_values($hits)));

$in = json_decode(file_get_contents('php://input'), true) ?: [];
$question = mb_substr(trim((string)($in['question'] ?? '')), 0, 600);
$lang = ($in['lang'] ?? 'de') === 'en' ? 'en' : 'de';
if ($question === '') { echo json_encode(['answer' => '']); exit; }

$ctx = $in['context'] ?? [];
$ctxText = '';
foreach (['name', 'day', 'triggers', 'done', 'catches'] as $k) {
  if (isset($ctx[$k])) { $ctxText .= $k . ': ' . mb_substr((string)$ctx[$k], 0, 120) . "\n"; }
}

$system = ($lang === 'en'
  ? "You are the friendly assistant inside NagelNEU, a free 21-day self-help app for adults who want to stop biting their nails. Answer in English, briefly (max. 120 words), warmly and practically. Stay on the topics of nail biting, hand care, habits, motivation and how to use the app (Caught it! button, 60-second Hands Stop, diary, voice notes, photos on days 1/7/14/21, PDF, Nibbler characters). For other topics, politely steer back. You give no medical diagnoses; with inflammation, pus or strong pain, recommend seeing a doctor. If someone mentions suicidal thoughts or self-harm, respond with care and point them to local emergency services or a crisis line."
  : "Du bist der freundliche Assistent in NagelNEU, einer kostenlosen 21-Tage-Selbsthilfe-App für Erwachsene, die mit dem Nägelkauen aufhören wollen. Antworte auf Deutsch, kurz (höchstens 120 Wörter), herzlich und praktisch, mit „du“. Bleib bei den Themen Nägelkauen, Handpflege, Gewohnheiten, Motivation und Bedienung der App (Knopf „Ertappt!“, 60-Sekunden-Hände-Stopp, Tagebuch, Sprachnotizen, Fotos an Tag 1/7/14/21, PDF, Knibbler-Figuren). Bei anderen Themen lenke freundlich zurück. Du stellst keine medizinischen Diagnosen; bei Entzündung, Eiter oder starken Schmerzen empfiehl eine Ärztin oder einen Arzt. Erwähnt jemand Suizidgedanken oder Selbstverletzung, antworte einfühlsam und nenne die TelefonSeelsorge 0800 111 0 111 sowie den Notruf 112.")
  . ($ctxText !== '' ? "\n\n" . ($lang === 'en' ? 'Current user data from the app:' : 'Aktuelle Daten der Person aus der App:') . "\n" . $ctxText : '');

$messages = [];
foreach (array_slice($in['history'] ?? [], -6) as $h) {
  $role = ($h['role'] ?? '') === 'assistant' ? 'assistant' : 'user';
  $text = mb_substr(trim((string)($h['text'] ?? '')), 0, 800);
  if ($text === '') continue;
  if ($messages && end($messages)['role'] === $role) { $messages[count($messages) - 1]['content'] .= "\n" . $text; continue; }
  $messages[] = ['role' => $role, 'content' => $text];
}
while ($messages && $messages[0]['role'] !== 'user') array_shift($messages);
if (!$messages || end($messages)['role'] !== 'user' || end($messages)['content'] !== $question) {
  if ($messages && end($messages)['role'] === 'user') array_pop($messages);
  $messages[] = ['role' => 'user', 'content' => $question];
}

$ch = curl_init('https://api.anthropic.com/v1/messages');
curl_setopt_array($ch, [
  CURLOPT_POST => true,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_TIMEOUT => 25,
  CURLOPT_HTTPHEADER => [
    'content-type: application/json',
    'x-api-key: ' . $key,
    'anthropic-version: 2023-06-01',
  ],
  CURLOPT_POSTFIELDS => json_encode([
    'model' => MODEL,
    'max_tokens' => 400,
    'system' => $system,
    'messages' => $messages,
  ]),
]);
$res = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

$answer = '';
if ($res !== false && $code === 200) {
  $j = json_decode($res, true);
  foreach (($j['content'] ?? []) as $c) { if (($c['type'] ?? '') === 'text') $answer .= $c['text']; }
}
echo json_encode(['answer' => trim($answer)], JSON_UNESCAPED_UNICODE);
