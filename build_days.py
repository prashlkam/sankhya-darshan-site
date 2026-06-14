# -*- coding: utf-8 -*-
"""Generates day1.html … day7.html for the Sankhya Satsang site."""

DEV = ["१", "२", "३", "४", "५", "६", "७"]

DAYS = [
  dict(
    title="प्रवेश — Why Sankhya?",
    sub="The satsang opens where Sankhya itself opens: with the honest admission of suffering, and the introduction of Maharshi Kapila, the adi-acharya of this darshana.",
    shloka=("दुःखत्रयाभिघाताज्जिज्ञासा तदभिघातके हेतौ ।<br>दृष्टे सापार्था चेन्नैकान्तात्यन्ततोऽभावात् ॥",
            "From the torment of the threefold suffering arises the desire to know the means of ending it. If you say visible remedies suffice — no, for they end nothing once and for all.",
            "साङ्ख्यकारिका १"),
    body="""
<h2>The threefold suffering</h2>
<p>The katha began not with cosmology but with daily life. Every human being, Bhaiji reminded the audience, is struck again and again by three kinds of dukha: <strong>adhyatmika</strong> — suffering arising within one's own body and mind, from illness to anxiety; <strong>adhibhautika</strong> — suffering caused by other beings, from a mosquito to a hostile neighbour; and <strong>adhidaivika</strong> — suffering from forces beyond anyone's control: flood, drought, fate. Medicine, money and caution can postpone these, never abolish them. The honest mind therefore asks: is there a remedy that is <em>ekanta</em> (certain) and <em>atyanta</em> (final)?</p>
<h2>Kapila Muni — the first teacher</h2>
<p>Sankhya's answer begins with its founder. Maharshi Kapila is no ordinary philosopher: the Bhagavat (3.24) reveres him as an avatara of Bhagwan himself, born to Kardama Rishi and Devahuti precisely to teach this knowledge. The Gita honours him by name — <em>siddhanam Kapilo munih</em> (10.26), "among the perfected, I am the sage Kapila." A darshana whose first acharya is counted among Bhagwan's vibhutis cannot be dry; it begins in compassion for suffering beings.</p>
<h2>Knowledge as the only final medicine</h2>
<p>The day closed on Sankhya's central claim: suffering persists because we misidentify — we take the seer to be the seen, the Self to be the body-mind. No external remedy can correct an internal error of recognition. Only <em>jnana</em> — precise, discriminative knowledge of what I am and what I am not — uproots dukha at its source. The seven days ahead would build that knowledge step by step, tattva by tattva.</p>
""",
  ),
  dict(
    title="पुरुष — The Witness",
    sub="Who is the one that suffers, sees, knows? Day two turns the lamp inward to Purusha — consciousness itself.",
    shloka=("प्रकृतेर्महांस्ततोऽहङ्कारस्तस्माद्गणश्च षोडशकः ।",
            "From Prakriti comes the Great One (mahat); from that, the I-maker; from that, the group of sixteen… — but before counting nature, Sankhya first establishes the one who counts: the Purusha.",
            "साङ्ख्यकारिका २२"),
    body="""
<h2>The seer is not the seen</h2>
<p>Everything we can observe — the body, its sensations, even thoughts and moods — is an <em>object</em> of awareness. Sankhya's razor: whatever is seen cannot be the seer. The eye sees forms but cannot see itself; the mind knows thoughts but is itself known by something more inward. That final, irreducible knower — never an object, always the subject — is <strong>Purusha</strong>.</p>
<h2>The marks of Purusha</h2>
<ul>
<li><strong>Chetan</strong> — it is consciousness itself, not a thing that <em>has</em> consciousness.</li>
<li><strong>Akarta</strong> — it does nothing; all action belongs to the gunas of Prakriti.</li>
<li><strong>Nirvikara</strong> — it never changes; childhood, youth and old age pass before it like scenes before a lamp.</li>
<li><strong>Sakshi</strong> — it is the witness: intimate to every experience, touched by none.</li>
<li><strong>Aneka</strong> — Sankhya holds the purushas to be many: each jiva a distinct witness, which is why one being's liberation does not liberate all.</li>
</ul>
<h2>The lamp in the theatre</h2>
<p>Bhaiji's gift was the analogy. The stage-lamp illumines the dance, the dancer, the audience — yet dances not, weeps not, applauds not. Remove the play and the lamp shines exactly as before. So is the Self amid the play of body and mind. The audience was sent home with one practice: through the day, quietly notice — <em>I am the one to whom this is appearing.</em></p>
""",
  ),
  dict(
    title="प्रकृति और त्रिगुण — Nature and the Three Gunas",
    sub="If the Self does nothing, who does everything? Day three introduces Prakriti and the three gunas from which the entire world-experience is woven.",
    shloka=("सत्त्वं रजस्तम इति गुणाः प्रकृतिसम्भवाः ।<br>निबध्नन्ति महाबाहो देहे देहिनमव्ययम् ॥",
            "Sattva, rajas and tamas — these gunas born of Prakriti, O mighty-armed, bind the imperishable dweller in the body.",
            "श्रीमद्भगवद्गीता १४.५"),
    body="""
<h2>The uncaused cause</h2>
<p><strong>Mula-Prakriti</strong> is Sankhya's second eternal: one, unconscious, infinitely potent — the root from which all twenty-three remaining tattvas evolve, itself evolved from nothing. Before creation she rests as perfect equilibrium of the three gunas; creation begins the instant that balance trembles in the presence of Purusha.</p>
<h2>The three strands</h2>
<ul>
<li><strong>सत्त्व Sattva</strong> — luminosity, clarity, harmony. In the mind: knowledge, contentment, lightness. Its bondage is subtle — attachment to happiness and to knowing.</li>
<li><strong>रजस् Rajas</strong> — motion, desire, effort. In the mind: ambition, restlessness, craving. It binds through attachment to action and its fruits.</li>
<li><strong>तमस् Tamas</strong> — inertia, concealment, heaviness. In the mind: dullness, sleep, delusion. It binds through negligence and stupor.</li>
</ul>
<p>No object or mood is purely one guna; everything is a ratio. A single mind moves through all three in a single hour — and recognising <em>which guna is presently speaking</em> is, Bhaiji stressed, the beginning of practical Sankhya in daily life.</p>
<h2>Why this matters for sadhana</h2>
<p>The gunas cannot be destroyed — they are Prakriti herself — but they can be cultured: increase sattva through ahara (food), sanga (company), and shravana (what one listens to — satsang itself being the supreme sattvic diet); let rajas serve sattva instead of ruling it; starve tamas of its occasions. Beyond even sattva lies the goal: to stand as the witness of all three.</p>
""",
  ),
  dict(
    title="सृष्टिक्रम — The Twenty-Five Tattvas",
    sub="The heart of the satsang: the precise order in which the universe unfolds from Prakriti — the great enumeration that gives Sankhya its name.",
    shloka=("प्रकृतेर्महांस्ततोऽहङ्कारस्तस्माद्गणश्च षोडशकः ।<br>तस्मादपि षोडशकात्पञ्चभ्यः पञ्च भूतानि ॥",
            "From Prakriti, the mahat; from that, ahankara; from that, the group of sixteen; and from five of those sixteen, the five gross elements.",
            "साङ्ख्यकारिका २२"),
    body="""
<h2>The order of unfoldment</h2>
<ol>
<li><strong>महत् / बुद्धि (3)</strong> — the first evolute: cosmic intelligence; in the individual, the faculty of determination and discernment.</li>
<li><strong>अहंकार (4)</strong> — the I-maker, which bends the universal into "me and mine."</li>
<li>From sattvic ahankara: <strong>मन (5)</strong>, the coordinating mind, and the <strong>five jnanendriyas (6–10)</strong> — powers of hearing, touch, sight, taste, smell — and <strong>five karmendriyas (11–15)</strong> — speech, grasping, locomotion, excretion, procreation.</li>
<li>From tamasic ahankara: the <strong>five tanmatras (16–20)</strong> — the subtle essences of sound, touch, form, taste and smell.</li>
<li>From the tanmatras: the <strong>five mahabhutas (21–25)</strong> — space, air, fire, water, earth — the gross stuff of the world.</li>
</ol>
<p>Add the two eternals — Purusha (1) and Mula-Prakriti (2) — and the count is complete: <strong>twenty-five tattvas</strong>. Study the full chart on the <a href="sankhya.html">Sankhya Darshan page</a>; Bhaiji had the audience recite the sequence aloud until it sat in memory like a sutra.</p>
<h2>The body as the universe in miniature</h2>
<p>The same order that builds the cosmos builds each of us: every human being carries all twenty-four principles of nature, presided over by one Purusha. This is why Sankhya calls the body a <em>kshetra</em>, a field — and why the Gita's thirteenth chapter, the Kshetra-Kshetrajna Vibhaga Yoga, reads as pure Sankhya. To know the map of the tattvas is to hold a mirror to oneself.</p>
""",
  ),
  dict(
    title="बन्धन — The Knot of Bondage",
    sub="If Purusha is ever-free and Prakriti is unconscious, who exactly is bound — and how? Day five examines the knot, and the analogy of the lame man and the blind man.",
    shloka=("तस्मान्न बध्यतेऽद्धा न मुच्यते नापि संसरति कश्चित् ।<br>संसरति बध्यते मुच्यते च नानाश्रया प्रकृतिः ॥",
            "Therefore no one is truly bound, no one liberated, no one transmigrates. It is Prakriti alone, in her many forms, who is bound, who transmigrates, who is released.",
            "साङ्ख्यकारिका ६२"),
    body="""
<h2>पङ्ग्वन्ध-न्याय — the lame man and the blind man</h2>
<p>Sankhya's most beloved analogy: a lame man who sees, carried on the shoulders of a blind man who walks. Purusha sees but cannot act; Prakriti acts but cannot see. Their association sets the whole journey of samsara in motion — and the journey ends when the destination is reached and the two part ways. Neither was ever truly the other; the partnership was for a purpose.</p>
<h2>The error called aviveka</h2>
<p>Bondage, then, is not a chain on the Self — nothing can chain the witness. It is a <em>mistake</em>: aviveka, the non-discrimination by which consciousness identifies with buddhi, ahankara and body, and says "I act, I suffer, I am fat, I am insulted." The crystal placed beside a red flower appears red; remove the flower and it was never coloured at all. So the Self appears bound by reflected qualities it never possessed.</p>
<h2>From mistake to medicine</h2>
<p>Because bondage is an error of knowledge, the remedy must be knowledge — <strong>विवेक viveka</strong>, the cultivated discrimination between drashta and drishya, seer and seen. Rituals purify, austerity strengthens, but only viveka uproots. The day ended with the question that day six would answer through the Bhagavat: how does this stern jnana become sweet enough for an ordinary heart to drink? The answer is bhakti — and a mother.</p>
""",
  ),
  dict(
    title="कपिल-देवहूति संवाद — When Sankhya Met Bhakti",
    sub="The emotional summit of the satsang: Bhagwan Kapila teaches Sankhya to his own mother Devahuti in the third canto of Shrimad Bhagavat.",
    shloka=("ज्ञानयोगश्च मन्निष्ठो नैर्गुण्यो भक्तिलक्षणः ।",
            "The yoga of knowledge fixed on Me, beyond the gunas, bears the mark of bhakti… — Kapila to Devahuti: jnana and bhakti are not rivals but one stream.",
            "श्रीमद्भागवत ३.२९ (कपिलोपदेश)"),
    body="""
<h2>A mother's question</h2>
<p>Kardama Rishi has departed to the forest; Devahuti, aging, turns to her divine son: <em>"Bhagavan, I am wearied by the darkness of this world of senses. You are my eye — show me the way across."</em> What follows in Bhagavat 3.25–3.33, the <strong>Kapilopadesha</strong>, is the most tender setting any philosophy was ever given: the founder of Sankhya teaching tattva-jnana not to scholars but to his own mother — and through her, to every ordinary seeker.</p>
<h2>Sankhya with Ishvara, jnana with prema</h2>
<p>Here the Bhagavat completes classical Sankhya: the twenty-five tattvas remain, but presiding over Prakriti stands Bhagwan himself — Prakriti is His shakti, the gunas His instruments, and the surest solvent of aviveka is <strong>satsang and bhakti</strong>. Kapila tells his mother that the company of sadhus and hearing of His lilas loosen the knot of the heart faster than austerity alone — for love absorbs the mind from the gunas more completely than effort ever suppresses them.</p>
<h2>The satsang's own mirror</h2>
<p>This day, by every memory, was the most moving of the seven — because the audience recognised itself. Every listener sitting before the telecast <em>was</em> Devahuti: not a philosopher, but a householder asking for the way across. And the teaching answered as Kapila answered — with rigour wrapped in tenderness. Devahuti, the Bhagavat records, attained the supreme goal through this very knowledge; the place of her sadhana is revered as Siddhapada — associated with present-day Siddhpur in Gujarat.</p>
""",
  ),
  dict(
    title="कैवल्य — Liberation, and the Dancer's Last Bow",
    sub="The samapan: viveka ripens into freedom, Prakriti withdraws like a dancer who has finished her performance, and Sankhya takes its seat within the Gita.",
    shloka=("रङ्गस्य दर्शयित्वा निवर्तते नर्तकी यथा नृत्यात् ।<br>पुरुषस्य तथात्मानं प्रकाश्य विनिवर्तते प्रकृतिः ॥",
            "As a dancer, having shown herself to the audience, withdraws from the dance — so Prakriti, having revealed herself to Purusha, withdraws.",
            "साङ्ख्यकारिका ५९"),
    body="""
<h2>The most generous verse in philosophy</h2>
<p>Sankhya's account of liberation is unique in its grace toward Prakriti. She is no temptress to be defeated; she is a performer whose entire dance existed <em>for the Purusha's awakening</em>. The Karika adds the famous words: "Nothing, I judge, is more modest than Prakriti — once she knows 'I have been seen,' she never again comes into the Purusha's view." Liberation is not a battle won but a performance completed.</p>
<h2>कैवल्य — aloneness that is fullness</h2>
<p><strong>Kaivalya</strong> means the Self abiding as itself alone — the witness no longer mistaking itself for the dance. Suffering ends not because the world is destroyed but because the false identification that hosted suffering has nowhere left to live. This is the ekanta, atyanta remedy that Day 1's question demanded.</p>
<h2>Sankhya's seat in the Gita — and the vida'i</h2>
<p>The satsang closed where the Gita begins its teaching: Chapter 2, <em>Sankhya Yoga</em> — "Never was there a time when I was not…" (2.12), "Weapons cut It not, fire burns It not…" (2.23). Shri Krishna gives Arjuna Sankhya's vision first, and only then karma, bhakti and dhyana as the means to live it. Jnana is the eye; bhakti, the feet. With the maha-aarti and the final bhajan, seven days of enumeration ended in what cannot be counted — and lakhs of viewers, like Devahuti, were left holding the way across.</p>
""",
  ),
]

HEADER = """<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Day {n} · {title_plain} · Sankhya Satsang</title>
<meta name="description" content="Day {n} of the Sankhya Shastra satsang by Pujya Shri Kiritbhai Ji (Aastha Channel, December 2006): {title_plain}.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Rozha+One&family=Martel:wght@400;600&family=Mukta:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><span class="om">ॐ</span>साङ्ख्य सत्संग</a>
    <nav class="main-nav" aria-label="Primary">
      <a href="index.html">Home</a>
      <a href="sankhya.html">Sankhya Darshan</a>
      <a href="day1.html">Day १</a>
      <a href="day2.html">२</a>
      <a href="day3.html">३</a>
      <a href="day4.html">४</a>
      <a href="day5.html">५</a>
      <a href="day6.html">६</a>
      <a href="day7.html">७</a>
      <a href="acharya.html">The Acharya</a>
    </nav>
  </div>
</header>
"""

FOOTER = """
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h4>साङ्ख्य सत्संग</h4>
        <p>A devotee's archive of the Sankhya Shastra satsang by Pujya Shri Kiritbhai Ji, telecast live on Aastha Channel in December 2006.</p>
      </div>
      <div>
        <h4>The Days</h4>
        <ul>
          <li><a href="day1.html">१ · Why Sankhya?</a></li>
          <li><a href="day2.html">२ · Purusha</a></li>
          <li><a href="day3.html">३ · Prakriti &amp; Gunas</a></li>
          <li><a href="day4.html">४ · The 25 Tattvas</a></li>
          <li><a href="day5.html">५ · Bondage</a></li>
          <li><a href="day6.html">६ · Kapila–Devahuti</a></li>
          <li><a href="day7.html">७ · Kaivalya</a></li>
        </ul>
      </div>
      <div>
        <h4>Study</h4>
        <ul>
          <li><a href="sankhya.html">Sankhya Darshan primer</a></li>
          <li><a href="acharya.html">About the Acharya</a></li>
        </ul>
      </div>
    </div>
    <p class="foot-note">This is a personal, non-commercial archive maintained by a devotee. Original telecast © Aastha Channel and the katha organisers. ॐ शान्तिः शान्तिः शान्तिः</p>
  </div>
</footer>

<script src="js/main.js"></script>
</body>
</html>
"""

PAGE = """{header}
<main>
  <div class="day-hero">
    <div class="wrap">
      <div class="day-num">{dev}</div>
      <h1>{title}</h1>
      <p class="day-sub">{sub}</p>
    </div>
  </div>

  <section class="band">
    <div class="wrap">
      <article class="teaching reveal">
        <div class="shloka">
          <div class="sa">{sh_sa}</div>
          <div class="tr">{sh_tr}</div>
          <div class="src">{sh_src}</div>
        </div>
        {body}
      </article>

      <div class="archive-note reveal">
        <strong>From the original telecast:</strong> the verbatim transcript, bhajans and video clips of Day {n} are being restored from the December 2006 archive recordings. To add them, place the files in the <code>media/</code> folder using the names below — the players will pick them up automatically.
      </div>

      <div class="media-block reveal">
        <h4>🎬 Video — Day {n} katha</h4>
        <video controls preload="none">
          <source src="media/day{n}-katha.mp4" type="video/mp4">
          Your browser does not support the video tag.
        </video>
        <p class="caption">Expected file: <code>media/day{n}-katha.mp4</code> — the day's katha recording from the telecast.</p>
      </div>

      <div class="media-block reveal">
        <h4>🎵 Bhajan — Day {n}</h4>
        <audio controls preload="none" src="media/day{n}-bhajan.mp3"></audio>
        <p class="caption">Expected file: <code>media/day{n}-bhajan.mp3</code> — the bhajan(s) sung during the day's satsang.</p>
      </div>

      <div class="media-block reveal">
        <h4>📜 Transcript — Day {n}</h4>
        <p class="caption">Paste the day's transcript here (Hindi or English), replacing this paragraph. Headings inside the transcript can use <code>&lt;h2&gt;</code> tags to match the page style.</p>
      </div>

      <div class="day-nav-row">
        <span>{prev}</span>
        <span>{nxt}</span>
      </div>
    </div>
  </section>
</main>
{footer}"""

import re

for i, d in enumerate(DAYS):
    n = i + 1
    title_plain = re.sub(r"[—-].*$", "", d["title"]).strip()
    prev = f'<a href="day{n-1}.html">← Day {DEV[n-2]}</a>' if n > 1 else '<a href="index.html">← Home</a>'
    nxt = f'<a href="day{n+1}.html">Day {DEV[n]} →</a>' if n < 7 else '<a href="sankhya.html">The Tattva Chart →</a>'
    html = PAGE.format(
        header=HEADER.format(n=n, title_plain=title_plain),
        dev=DEV[i], title=d["title"], sub=d["sub"],
        sh_sa=d["shloka"][0], sh_tr=d["shloka"][1], sh_src=d["shloka"][2],
        body=d["body"], n=n, prev=prev, nxt=nxt, footer=FOOTER,
    )
    with open(f"day{n}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote day{n}.html ({len(html)} bytes)")
