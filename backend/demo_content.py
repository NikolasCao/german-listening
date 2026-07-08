"""
内置 Demo 内容 —— 无需 API Key 即可体验完整功能
6 个 CEFR 等级 × 3 种题型 = 18 套练习，难度严格匹配 CEFR 标准
"""

DEMO_AVAILABLE = True

# ==================== Demo 练习库 ====================
DEMO_EXERCISES = [

    # ==================== A1 ====================

    # ---------- A1 · 选择题 · 问候 ----------
    {
        "title": "Begrüßung im Supermarkt",
        "description": "Ein einfacher Dialog über Begrüßung und Small Talk.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Anna", "gender": "female"},
            {"name": "Tom", "gender": "male"},
        ],
        "text_segments": [
            {"speaker": "Anna", "text": "Hallo! Guten Morgen!"},
            {"speaker": "Tom", "text": "Guten Morgen! Wie heißt du?"},
            {"speaker": "Anna", "text": "Ich heiße Anna. Und du?"},
            {"speaker": "Tom", "text": "Ich bin Tom. Wo wohnst du?"},
            {"speaker": "Anna", "text": "Ich wohne in Berlin. Und du?"},
            {"speaker": "Tom", "text": "Ich wohne auch in Berlin. Schön!"},
        ],
        "questions": [
            {"id": 1, "type": "multiple_choice", "question": "Wie heißt die Frau?",
             "options": ["A. Tom", "B. Anna", "C. Berlin", "D. Guten Morgen"], "answer": "B"},
            {"id": 2, "type": "multiple_choice", "question": "Wo wohnt Anna?",
             "options": ["A. In München", "B. In Hamburg", "C. In Berlin", "D. In Köln"], "answer": "C"},
            {"id": 3, "type": "multiple_choice", "question": "Was sagt Tom am Anfang?",
             "options": ["A. Guten Abend", "B. Guten Morgen", "C. Gute Nacht", "D. Tschüss"], "answer": "B"},
            {"id": 4, "type": "multiple_choice", "question": "Wie heißt der Mann?",
             "options": ["A. Tom", "B. Anna", "C. Peter", "D. Max"], "answer": "A"},
            {"id": 5, "type": "multiple_choice", "question": "Wo wohnt Tom?",
             "options": ["A. In München", "B. In Berlin", "C. In Frankfurt", "D. In Stuttgart"], "answer": "B"},
        ],
    },

    # ---------- A1 · 填空题 · 餐厅 ----------
    {
        "title": "Im Restaurant",
        "description": "Ein einfacher Dialog im Restaurant.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Kellner", "gender": "male"},
            {"name": "Kunde", "gender": "female"},
        ],
        "text_segments": [
            {"speaker": "Kellner", "text": "Guten Tag! Was möchten Sie trinken?"},
            {"speaker": "Kunde", "text": "Ich möchte einen Kaffee, bitte."},
            {"speaker": "Kellner", "text": "Einen Kaffee. Möchten Sie auch etwas essen?"},
            {"speaker": "Kunde", "text": "Ja, ich nehme ein Brötchen mit Käse."},
            {"speaker": "Kellner", "text": "Gut. Ein Kaffee und ein Brötchen mit Käse."},
            {"speaker": "Kunde", "text": "Ja, genau. Vielen Dank!"},
        ],
        "questions": [
            {"id": 1, "type": "fill_blank", "question": "Ich möchte einen ___, bitte.", "answer": "Kaffee"},
            {"id": 2, "type": "fill_blank", "question": "Ich nehme ein Brötchen mit ___.", "answer": "Käse"},
            {"id": 3, "type": "fill_blank", "question": "Was möchten Sie ___?", "answer": "trinken"},
            {"id": 4, "type": "fill_blank", "question": "Ja, ich nehme ein ___ mit Käse.", "answer": "Brötchen"},
            {"id": 5, "type": "fill_blank", "question": "Vielen ___!", "answer": "Dank"},
        ],
    },

    # ---------- A1 · 解答题 · 日常 ----------
    {
        "title": "Mein Tag",
        "description": "Ein Monolog über den Tagesablauf.",
        "text_type": "monologue",
        "speakers": [{"name": "Lisa", "gender": "female"}],
        "text_segments": [
            {"speaker": "Lisa", "text": "Ich heiße Lisa und ich bin Studentin."},
            {"speaker": "Lisa", "text": "Jeden Morgen stehe ich um sieben Uhr auf."},
            {"speaker": "Lisa", "text": "Ich trinke Kaffee und esse Brot."},
            {"speaker": "Lisa", "text": "Dann gehe ich zur Universität."},
            {"speaker": "Lisa", "text": "Am Nachmittag lerne ich Deutsch."},
        ],
        "questions": [
            {"id": 1, "type": "open_ended", "question": "Wie heißt die Person?", "answer": "Lisa."},
            {"id": 2, "type": "open_ended", "question": "Wann steht Lisa auf?", "answer": "Um sieben Uhr."},
            {"id": 3, "type": "open_ended", "question": "Was trinkt Lisa am Morgen?", "answer": "Kaffee."},
            {"id": 4, "type": "open_ended", "question": "Was isst sie?", "answer": "Brot."},
            {"id": 5, "type": "open_ended", "question": "Was macht Lisa am Nachmittag?", "answer": "Sie lernt Deutsch."},
        ],
    },

    # ==================== A2 ====================

    # ---------- A2 · 选择题 · 休闲活动 ----------
    {
        "title": "Freizeit am Wochenende",
        "description": "Zwei Freunde sprechen über ihre Wochenendpläne.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Julia", "gender": "female"},
            {"name": "Felix", "gender": "male"},
        ],
        "text_segments": [
            {"speaker": "Julia", "text": "Hallo Felix! Was hast du am Wochenende vor?"},
            {"speaker": "Felix", "text": "Am Samstag spiele ich Fußball mit meinem Verein. Und du?"},
            {"speaker": "Julia", "text": "Ich gehe am Samstag ins Kino. Es gibt einen neuen Film."},
            {"speaker": "Felix", "text": "Das klingt interessant! Welchen Film willst du sehen?"},
            {"speaker": "Julia", "text": "Einen Komödienfilm. Am Sonntag besuche ich meine Großeltern."},
            {"speaker": "Felix", "text": "Das ist schön. Ich bleibe am Sonntag zu Hause und lese ein Buch."},
        ],
        "questions": [
            {"id": 1, "type": "multiple_choice", "question": "Was macht Felix am Samstag?",
             "options": ["A. Er geht ins Kino", "B. Er spielt Fußball", "C. Er besucht Großeltern", "D. Er liest ein Buch"], "answer": "B"},
            {"id": 2, "type": "multiple_choice", "question": "Was möchte Julia im Kino sehen?",
             "options": ["A. Einen Actionfilm", "B. Einen Horrorfilm", "C. Einen Komödienfilm", "D. Einen Dokumentarfilm"], "answer": "C"},
            {"id": 3, "type": "multiple_choice", "question": "Wen besucht Julia am Sonntag?",
             "options": ["A. Ihre Eltern", "B. Ihre Freunde", "C. Ihre Großeltern", "D. Ihren Bruder"], "answer": "C"},
            {"id": 4, "type": "multiple_choice", "question": "Was macht Felix am Sonntag?",
             "options": ["A. Er spielt Fußball", "B. Er geht ins Kino", "C. Er bleibt zu Hause und liest", "D. Er besucht Julia"], "answer": "C"},
            {"id": 5, "type": "multiple_choice", "question": "Mit wem spielt Felix Fußball?",
             "options": ["A. Mit Julia", "B. Mit seinem Verein", "C. Mit seinen Großeltern", "D. Allein"], "answer": "B"},
        ],
    },

    # ---------- A2 · 填空题 · 购物 ----------
    {
        "title": "Einkaufen auf dem Markt",
        "description": "Ein Dialog über Einkaufen auf dem Wochenmarkt.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Maria", "gender": "female"},
            {"name": "Verkäufer", "gender": "male"},
        ],
        "text_segments": [
            {"speaker": "Maria", "text": "Guten Tag! Was kostet ein Kilo Äpfel?"},
            {"speaker": "Verkäufer", "text": "Die Äpfel kosten zwei Euro fünfzig pro Kilo."},
            {"speaker": "Maria", "text": "Ich nehme ein Kilo. Haben Sie auch Bananen?"},
            {"speaker": "Verkäufer", "text": "Ja, die Bananen kosten drei Euro pro Kilo."},
            {"speaker": "Maria", "text": "Gut, ich nehme auch ein Kilo Bananen."},
            {"speaker": "Verkäufer", "text": "Das macht zusammen fünf Euro fünfzig."},
            {"speaker": "Maria", "text": "Hier ist das Geld. Vielen Dank!"},
        ],
        "questions": [
            {"id": 1, "type": "fill_blank", "question": "Die Äpfel kosten ___ Euro fünfzig pro Kilo.", "answer": "zwei"},
            {"id": 2, "type": "fill_blank", "question": "Die Bananen kosten ___ Euro pro Kilo.", "answer": "drei"},
            {"id": 3, "type": "fill_blank", "question": "Das macht zusammen ___ Euro fünfzig.", "answer": "fünf"},
            {"id": 4, "type": "fill_blank", "question": "Maria kauft ein Kilo Äpfel und ein Kilo ___.", "answer": "Bananen"},
            {"id": 5, "type": "fill_blank", "question": "Maria sagt: Hier ist das ___.", "answer": "Geld"},
        ],
    },

    # ---------- A2 · 解答题 · 周末计划 ----------
    {
        "title": "Pläne für den Urlaub",
        "description": "Ein Gespräch über Urlaubspläne.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Sabine", "gender": "female"},
            {"name": "Markus", "gender": "male"},
        ],
        "text_segments": [
            {"speaker": "Sabine", "text": "Hallo Markus! Wohin fährst du dieses Jahr in den Urlaub?"},
            {"speaker": "Markus", "text": "Ich fahre nach Spanien, an den Strand. Und du?"},
            {"speaker": "Sabine", "text": "Ich bleibe in Deutschland und besuche meine Freunde in Köln."},
            {"speaker": "Markus", "text": "Das ist auch schön. Wie lange bleibst du in Köln?"},
            {"speaker": "Sabine", "text": "Zwei Wochen. Wir wollen zusammen das Museum besuchen und durch die Stadt spazieren."},
            {"speaker": "Markus", "text": "Das klingt toll! Ich wünsche dir viel Spaß!"},
        ],
        "questions": [
            {"id": 1, "type": "open_ended", "question": "Wohin fährt Markus in den Urlaub?", "answer": "Nach Spanien, an den Strand."},
            {"id": 2, "type": "open_ended", "question": "Was macht Sabine in ihrem Urlaub?", "answer": "Sie bleibt in Deutschland und besucht ihre Freunde in Köln."},
            {"id": 3, "type": "open_ended", "question": "Wie lange bleibt Sabine in Köln?", "answer": "Zwei Wochen."},
            {"id": 4, "type": "open_ended", "question": "Was wollen Sabine und ihre Freunde zusammen machen?", "answer": "Sie wollen das Museum besuchen und durch die Stadt spazieren."},
            {"id": 5, "type": "open_ended", "question": "Was wünscht Markus Sabine zum Schluss?", "answer": "Viel Spaß."},
        ],
    },

    # ==================== B1 ====================

    # ---------- B1 · 选择题 · 面试 ----------
    {
        "title": "Bewerbungsgespräch",
        "description": "Ein Vorstellungsgespräch für eine Stelle als Marketing-Assistentin.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Herr Wagner", "gender": "male"},
            {"name": "Frau Becker", "gender": "female"},
        ],
        "text_segments": [
            {"speaker": "Herr Wagner", "text": "Guten Tag, Frau Becker. Schön, dass Sie gekommen sind. Erzählen Sie doch kurz von sich."},
            {"speaker": "Frau Becker", "text": "Gerne. Ich habe Kommunikationswissenschaften in Leipzig studiert und danach zwei Jahre in einer Werbeagentur in Hamburg gearbeitet."},
            {"speaker": "Herr Wagner", "text": "Das klingt vielversprechend. Warum möchten Sie eigentlich unseren Firmen wechseln?"},
            {"speaker": "Frau Becker", "text": "In meiner jetzigen Position habe ich mich vor allem auf Social-Media-Marketing konzentriert. Ich würde aber gerne mehr im Bereich der strategischen Markenführung arbeiten, und das ist genau Ihre Spezialität."},
            {"speaker": "Herr Wagner", "text": "Verstehe. Welche Stärken würden Sie sich selbst zuschreiben?"},
            {"speaker": "Frau Becker", "text": "Ich bin sehr analytisch und arbeite gerne im Team. Außerdem spreche ich fließend Englisch und Französisch, was bei internationalen Kunden sicher von Vorteil ist."},
            {"speaker": "Herr Wagner", "text": "Das könnte tatsächlich nützlich sein. Haben Sie noch Fragen an uns?"},
            {"speaker": "Frau Becker", "text": "Ja, ich würde gerne wissen, wie die Zusammenarbeit zwischen den verschiedenen Abteilungen bei Ihnen organisiert ist."},
        ],
        "questions": [
            {"id": 1, "type": "multiple_choice", "question": "Was hat Frau Becker studiert?",
             "options": ["A. Wirtschaftswissenschaften in München", "B. Kommunikationswissenschaften in Leipzig",
                         "C. Marketing in Hamburg", "D. Informatik in Berlin"], "answer": "B"},
            {"id": 2, "type": "multiple_choice", "question": "Warum möchte Frau Becker die Firma wechseln?",
             "options": ["A. Sie ist unzufrieden mit ihrem Chef", "B. Sie möchte mehr Gehalt",
                         "C. Sie möchte im Bereich strategischer Markenführung arbeiten", "D. Sie möchte näher bei ihrer Familie wohnen"], "answer": "C"},
            {"id": 3, "type": "multiple_choice", "question": "Welche Stärken nennt Frau Becker?",
             "options": ["A. Kreativität und Selbstständigkeit", "B. Analytisches Denken und Teamfähigkeit",
                         "C. Verkaufstalent und Durchsetzungsvermögen", "D. Organisation und Pünktlichkeit"], "answer": "B"},
            {"id": 4, "type": "multiple_choice", "question": "Welche Sprachen spricht Frau Becker?",
             "options": ["A. Deutsch und Englisch", "B. Deutsch, Englisch und Spanisch",
                         "C. Deutsch, Englisch und Französisch", "D. Deutsch und Französisch"], "answer": "C"},
            {"id": 5, "type": "multiple_choice", "question": "Was möchte Frau Becker am Ende wissen?",
             "options": ["A. Wie hoch das Gehalt ist", "B. Wie die Zusammenarbeit zwischen den Abteilungen organisiert ist",
                         "C. Wann sie anfangen kann", "D. Wie viele Urlaubstage sie hat"], "answer": "B"},
        ],
    },

    # ---------- B1 · 填空题 · 旅行 ----------
    {
        "title": "Eine Reise nach München",
        "description": "Ein Gespräch über Reisepläne nach München.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Lisa", "gender": "female"},
            {"name": "Max", "gender": "male"},
        ],
        "text_segments": [
            {"speaker": "Lisa", "text": "Hallo Max! Ich plane eine Reise nach München und wollte fragen, ob du Lust hast mitzukommen."},
            {"speaker": "Max", "text": "Ja, gerne! Wann wollt ihr denn fahren?"},
            {"speaker": "Lisa", "text": "Ich dachte an nächstes Wochenende, also vom Freitag bis zum Sonntag."},
            {"speaker": "Max", "text": "Das passt mir gut. Wie wollen wir reisen? Mit dem Zug wäre es am bequemsten, finde ich."},
            {"speaker": "Lisa", "text": "Stimmt, aber das Ticket ist ziemlich teuer. Wenn wir mit dem Auto fahren, könnten wir auch unterwegs anhalten."},
            {"speaker": "Max", "text": "Das ist ein guter Punkt. Wir könnten die Fahrt mit einem Zwischenstopp in Nürnberg verbinden."},
            {"speaker": "Lisa", "text": "Hervorragende Idee! Ich habe schon gehört, dass die Altstadt dort sehr schön sein soll."},
            {"speaker": "Max", "text": "Dann ist entschieden. Ich übernehme das Fahren, wenn du für die Unterkunft sorgst."},
        ],
        "questions": [
            {"id": 1, "type": "fill_blank", "question": "Ich plane eine ___ nach München.", "answer": "Reise"},
            {"id": 2, "type": "fill_blank", "question": "Das Ticket ist ziemlich ___.", "answer": "teuer"},
            {"id": 3, "type": "fill_blank", "question": "Wir könnten die Fahrt mit einem ___ in Nürnberg verbinden.", "answer": "Zwischenstopp"},
            {"id": 4, "type": "fill_blank", "question": "Die ___ dort soll sehr schön sein.", "answer": "Altstadt"},
            {"id": 5, "type": "fill_blank", "question": "Ich übernehme das ___, wenn du für die Unterkunft sorgst.", "answer": "Fahren"},
        ],
    },

    # ---------- B1 · 解答题 · 环境讨论 ----------
    {
        "title": "Diskussion über Mülltrennung",
        "description": "Zwei Nachbarn diskutieren über das Thema Mülltrennung.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Daniel", "gender": "male"},
            {"name": "Petra", "gender": "female"},
        ],
        "text_segments": [
            {"speaker": "Daniel", "text": "Sag mal Petra, hast du eigentlich gesehen, wie die Leute im Haus ihren Müll trennen? Das wird oft nicht richtig gemacht."},
            {"speaker": "Petra", "text": "Ja, das ist mir auch aufgefallen. Besonders beim Plastik wird oft alles in eine Tonne geworfen, ohne darauf zu achten, ob es recycelbar ist."},
            {"speaker": "Daniel", "text": "Genau. Ich finde, die Stadt sollte eine bessere Aufklärung betreiben, damit jeder weiß, was in welche Tonne gehört."},
            {"speaker": "Petra", "text": "Da stimme ich dir zu. Außerdem wäre es sinnvoll, wenn in jedem Haus kleine Hinweisschilder aufgehängt würden."},
            {"speaker": "Daniel", "text": "Das wäre ein guter Anfang. Aber ich glaube, das eigentliche Problem ist, dass viele Menschen das Gefühl haben, dass ihre Müßtrennung sowieso nichts bringt."},
            {"speaker": "Petra", "text": "Das ist leider wahr. Wenn man bedenkt, wie viel Müll wir jeden Tag produzieren, wird einem schon bewusst, dass jeder seinen Beitrag leisten muss."},
        ],
        "questions": [
            {"id": 1, "type": "open_ended", "question": "Was ist Daniel und Petra beim Mülltrennen im Haus aufgefallen?", "answer": "Besonders beim Plastik wird oft alles in eine Tonne geworfen, ohne darauf zu achten, ob es recycelbar ist."},
            {"id": 2, "type": "open_ended", "question": "Was schlägt Daniel vor, um die Situation zu verbessern?", "answer": "Die Stadt sollte eine bessere Aufklärung betreiben, damit jeder weiß, was in welche Tonne gehört."},
            {"id": 3, "type": "open_ended", "question": "Was hält Petra für sinnvoll?", "answer": "In jedem Haus sollten kleine Hinweisschilder aufgehängt werden."},
            {"id": 4, "type": "open_ended", "question": "Was ist laut Daniel das eigentliche Problem?", "answer": "Viele Menschen haben das Gefühl, dass ihre Mülltrennung sowieso nichts bringt."},
            {"id": 5, "type": "open_ended", "question": "Was wird Petra bewusst, wenn sie an die Müllmenge denkt?", "answer": "Dass jeder seinen Beitrag leisten muss, wenn man bedenkt, wie viel Müll man jeden Tag produziert."},
        ],
    },

    # ==================== B2 ====================

    # ---------- B2 · 选择题 · 环境保护 ----------
    {
        "title": "Umweltschutz im Alltag",
        "description": "Ein Interview über umweltfreundliche Gewohnheiten.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Journalist", "gender": "male"},
            {"name": "Sophie", "gender": "female"},
        ],
        "text_segments": [
            {"speaker": "Journalist", "text": "Frau Müller, Sie gelten als Vorbild im Bereich Umweltschutz. Was motiviert Sie dazu?"},
            {"speaker": "Sophie", "text": "Ich habe mich bereits vor Jahren mit dem Thema Klimawandel auseinandergesetzt. Dabei wurde mir klar, dass jeder Einzelne einen Beitrag leisten kann."},
            {"speaker": "Journalist", "text": "Was tun Sie konkret im Alltag?"},
            {"speaker": "Sophie", "text": "Ich verzichte komplett auf Plastikverpackungen, fahre mit dem Fahrrad zur Arbeit und beziehe Ökostrom. Außerdem kaufe ich ausschließlich regionale Produkte."},
            {"speaker": "Journalist", "text": "Das klingt nach erheblichem Aufwand. Ist das nicht mühsam?"},
            {"speaker": "Sophie", "text": "Anfangs war es gewöhnungsbedürftig, aber mittlerweile ist es zur Routine geworden. Das gute Gefühl, etwas für die Umwelt zu tun, wiegt den Aufwand bei weitem auf."},
            {"speaker": "Journalist", "text": "Was würden Sie anderen raten?"},
            {"speaker": "Sophie", "text": "Ich empfehle, mit kleinen Schritten anzufangen. Man muss nicht von heute auf morgen alles ändern. Jeder noch so kleine Beitrag zählt."},
        ],
        "questions": [
            {"id": 1, "type": "multiple_choice", "question": "Was motiviert Frau Müller zum Umweltschutz?",
             "options": ["A. Die Regierung hat es vorgeschrieben", "B. Sie hat sich mit dem Klimawandel auseinandergesetzt",
                         "C. Ihre Familie hat sie dazu gezwungen", "D. Sie wollte Geld sparen"], "answer": "B"},
            {"id": 2, "type": "multiple_choice", "question": "Welche Maßnahme gehört NICHT zu Sophies Gewohnheiten?",
             "options": ["A. Verzicht auf Plastikverpackungen", "B. Radfahren zur Arbeit",
                         "C. Kauf von importierten Produkten", "D. Bezug von Ökostrom"], "answer": "C"},
            {"id": 3, "type": "multiple_choice", "question": "Wie fand Sophie die Umstellung am Anfang?",
             "options": ["A. Sehr einfach von Anfang an", "B. Gewöhnungsbedürftig",
                         "C. Unmöglich", "D. Frustrierend und sinnlos"], "answer": "B"},
            {"id": 4, "type": "multiple_choice", "question": "Was rät Sophie anderen Menschen?",
             "options": ["A. Alles sofort zu ändern", "B. Gar nichts zu tun",
                         "C. Mit kleinen Schritten anzufangen", "D. Nur auf die Regierung zu warten"], "answer": "C"},
            {"id": 5, "type": "multiple_choice", "question": "Welche Produkte kauft Sophie ausschließlich?",
             "options": ["A. Importierte Produkte", "B. Regionale Produkte",
                         "C. Bioprodukte aus dem Ausland", "D. Günstigste Produkte"], "answer": "B"},
        ],
    },

    # ---------- B2 · 填空题 · 工作世界 ----------
    {
        "title": "Veränderungen in der Arbeitswelt",
        "description": "Ein Gespräch über neue Arbeitsmodelle.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Moderator", "gender": "male"},
            {"name": "Dr. Hoffmann", "gender": "female"},
        ],
        "text_segments": [
            {"speaker": "Moderator", "text": "Frau Dr. Hoffmann, die Arbeitswelt hat sich in den letzten Jahren stark verändert. Was sind die wichtigsten Trends?"},
            {"speaker": "Dr. Hoffmann", "text": "Der wohl bedeutendste Trend ist die Zunahme von Homeoffice. Seit der Pandemie arbeiten deutlich mehr Menschen regelmäßig von zu Hause aus."},
            {"speaker": "Moderator", "text": "Wird das nicht als Belastung empfunden, wenn Beruf und Privatleben verschwimmen?"},
            {"speaker": "Dr. Hoffmann", "text": "Das ist ein berechtigter Einwand. Es erfordert tatsächlich viel Selbstdisziplin. Wenn man aber klare Strukturen schafft, überwiegen meiner Meinung nach die Vorteile deutlich."},
            {"speaker": "Moderator", "text": "Welche Vorteile meinen Sie genau?"},
            {"speaker": "Dr. Hoffmann", "text": "Man spart Zeit für den Arbeitsweg, kann den Tag flexibler gestalten und ist oft produktiver, weil man weniger Ablenkung hat durch Kollegen."},
            {"speaker": "Moderator", "text": "Glauben Sie, dass dieses Modell sich langfristig durchsetzen wird?"},
            {"speaker": "Dr. Hoffmann", "text": "Ich bin davon überzeugt. Viele Unternehmen haben bereits erkannt, dass flexible Arbeitsmodelle nicht nur den Mitarbeitern zugutekommen, sondern auch die Bindung an das Unternehmen stärken."},
        ],
        "questions": [
            {"id": 1, "type": "fill_blank", "question": "Der bedeutendste Trend ist die Zunahme von ___.", "answer": "Homeoffice"},
            {"id": 2, "type": "fill_blank", "question": "Beruf und ___ verschwimmen.", "answer": "Privatleben"},
            {"id": 3, "type": "fill_blank", "question": "Es erfordert viel ___.", "answer": "Selbstdisziplin"},
            {"id": 4, "type": "fill_blank", "question": "Man spart Zeit für den ___.", "answer": "Arbeitsweg"},
            {"id": 5, "type": "fill_blank", "question": "Flexible Arbeitsmodelle stärken die ___ an das Unternehmen.", "answer": "Bindung"},
        ],
    },

    # ---------- B2 · 解答题 · 教育体系 ----------
    {
        "title": "Das deutsche Bildungssystem",
        "description": "Ein Gespräch über Vor- und Nachteile des deutschen Bildungssystems.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Thomas", "gender": "male"},
            {"name": "Claudia", "gender": "female"},
        ],
        "text_segments": [
            {"speaker": "Thomas", "text": "Claudia, du arbeitest doch im Bildungsbereich. Wie beurteilst du eigentlich das aktuelle deutsche Bildungssystem?"},
            {"speaker": "Claudia", "text": "Das ist eine schwierige Frage. Einerseits bietet das System eine solide Grundausbildung und die duale Berufsausbildung ist international anerkannt. Andererseits finde ich die frühe Selektion nach der vierten Klasse problematisch."},
            {"speaker": "Thomas", "text": "Du meinst die Aufteilung in Gymnasium, Realschule und Hauptschule?"},
            {"speaker": "Claudia", "text": "Genau. Mit zehn Jahren wird entschieden, welchen Bildungsweg ein Kind einschlägt. Das ist meiner Meinung nach zu früh, um das gesamte Potenzial eines Kindes zu erkennen."},
            {"speaker": "Thomas", "text": "Aber argumentieren Befürworter nicht, dass dadurch gezielter gefördert werden kann?"},
            {"speaker": "Claudia", "text": "Das stimmt, und das ist auch ein berechtigtes Argument. Dennoch zeigen Studien, dass Kinder aus bildungsfernen Familien bei dieser frühen Selektion benachteiligt werden. Das verstärkt die soziale Ungleichheit, was eigentlich vermieden werden sollte."},
            {"speaker": "Thomas", "text": "Was würdest du denn als Alternative vorschlagen?"},
            {"speaker": "Claudia", "text": "Ich plädiere für eine längere gemeinsame Schulzeit, mindestens bis zur sechsten Klasse. So hätten alle Kinder mehr Zeit, sich zu entwickeln, und die Lehrer könnten fundiertere Empfehlungen aussprechen."},
        ],
        "questions": [
            {"id": 1, "type": "open_ended", "question": "Was hält Claudia für problematisch am deutschen Bildungssystem?", "answer": "Die frühe Selektion nach der vierten Klasse, bei der mit zehn Jahren über den Bildungsweg entschieden wird."},
            {"id": 2, "type": "open_ended", "question": "Welches Argument führen Befürworter der frühen Selektion an?", "answer": "Dass durch die Aufteilung gezielter gefördert werden kann."},
            {"id": 3, "type": "open_ended", "question": "Was zeigen Studien laut Claudia?", "answer": "Kinder aus bildungsfernen Familien werden bei der frühen Selektion benachteiligt, was die soziale Ungleichheit verstärkt."},
            {"id": 4, "type": "open_ended", "question": "Welchen Vorteil des deutschen Systems erwähnt Claudia?", "answer": "Die solide Grundausbildung und die duale Berufsausbildung, die international anerkannt ist."},
            {"id": 5, "type": "open_ended", "question": "Was schlägt Claudia als Alternative vor?", "answer": "Eine längere gemeinsame Schulzeit, mindestens bis zur sechsten Klasse, damit alle Kinder mehr Zeit haben, sich zu entwickeln."},
        ],
    },

    # ==================== C1 ====================

    # ---------- C1 · 选择题 · 数字化 ----------
    {
        "title": "Die Digitalisierung der Gesellschaft",
        "description": "Ein Vortrag über die Auswirkungen der Digitalisierung.",
        "text_type": "monologue",
        "speakers": [{"name": "Professor Weber", "gender": "male"}],
        "text_segments": [
            {"speaker": "Professor Weber", "text": "Meine Damen und Herren, die Digitalisierung hat unsere Gesellschaft in den vergangenen Jahrzehnten grundlegend transformiert und dieser Prozess ist keineswegs abgeschlossen."},
            {"speaker": "Professor Weber", "text": "Während früher die physische Präsenz am Arbeitsplatz obligatorisch war, ermöglichen moderne Kommunikationstechnologien mittlerweile ein ortsunabhängiges Arbeiten, das die konventionellen Vorstellungen von Arbeitszeit und Arbeitsort zunehmend obsolet erscheinen lässt."},
            {"speaker": "Professor Weber", "text": "Diese Entwicklung birgt jedoch nicht nur Chancen, sondern auch erhebliche Herausforderungen. Die permanente Erreichbarkeit führt bei vielen Beschäftigten zu einer fortschreitenden Entgrenzung der Lebensbereiche, was nicht selten in chronische Erschöpfungszustände mündet."},
            {"speaker": "Professor Weber", "text": "Zudem müssen sich Arbeitnehmer kontinuierlich weiterbilden, um mit dem rasanten technologischen Fortschritt Schritt halten zu können. Die Halbwertszeit von Fachwissen wird zunehmend kürzer, was an die Lernfähigkeit und Adaptionsbereitschaft jedes Einzelnen ungeahnte Anforderungen stellt."},
            {"speaker": "Professor Weber", "text": "Es ist daher unabdingbar, dass sowohl Arbeitgeber als auch Arbeitnehmer proaktiv Strategien entwickeln, um mit diesen Veränderungen konstruktiv umzugehen, ohne dabei die mentale Gesundheit zu vernachlässigen oder die soziale Kohäsion zu gefährden."},
        ],
        "questions": [
            {"id": 1, "type": "multiple_choice", "question": "Was stellt Professor Weber über den Digitalisierungsprozess fest?",
             "options": ["A. Er ist abgeschlossen", "B. Er ist keineswegs abgeschlossen",
                         "C. Er ist gescheitert", "D. Er wurde gestoppt"], "answer": "B"},
            {"id": 2, "type": "multiple_choice", "question": "Welche Herausforderung entsteht durch permanente Erreichbarkeit?",
             "options": ["A. Höhere Produktivität", "B. Bessere Work-Life-Balance",
                         "C. Entgrenzung der Lebensbereiche und Erschöpfungszustände", "D. Geringere Arbeitsbelastung"], "answer": "C"},
            {"id": 3, "type": "multiple_choice", "question": "Was passiert mit der Halbwertszeit von Fachwissen?",
             "options": ["A. Sie wird länger", "B. Sie bleibt gleich",
                         "C. Sie wird zunehmend kürzer", "D. Sie ist irrelevant"], "answer": "C"},
            {"id": 4, "type": "multiple_choice", "question": "Was fordert Professor Weber von Arbeitgebern und Arbeitnehmern?",
             "options": ["A. Die Digitalisierung zu stoppen", "B. Proaktiv Strategien zu entwickeln",
                         "C. Nur noch remote zu arbeiten", "D. Auf staatliche Hilfe zu warten"], "answer": "B"},
            {"id": 5, "type": "multiple_choice", "question": "Was soll bei den Strategien nicht vernachlässigt werden?",
             "options": ["A. Die finanzielle Bildung", "B. Die mentale Gesundheit und soziale Kohäsion",
                         "C. Die technische Infrastruktur", "D. Die internationale Wettbewerbsfähigkeit"], "answer": "B"},
        ],
    },

    # ---------- C1 · 填空题 · 未来工作 ----------
    {
        "title": "Die Zukunft der Arbeitswelt",
        "description": "Ein Vortrag über die Veränderungen der Arbeitswelt durch Digitalisierung.",
        "text_type": "monologue",
        "speakers": [{"name": "Professor Weber", "gender": "male"}],
        "text_segments": [
            {"speaker": "Professor Weber", "text": "Meine Damen und Herren, die Digitalisierung hat unsere Arbeitswelt in den vergangenen Jahrzehnten grundlegend transformiert."},
            {"speaker": "Professor Weber", "text": "Während früher die Präsenz am Arbeitsplatz obligatorisch war, ermöglichen moderne Technologien mittlerweile ein flexibles Arbeiten von nahezu jedem Ort der Welt."},
            {"speaker": "Professor Weber", "text": "Diese Entwicklung birgt jedoch nicht nur Chancen, sondern auch erhebliche Herausforderungen. Die ständige Erreichbarkeit führt bei vielen Beschäftigten zu einer zunehmenden Verschwimmung der Grenze zwischen Berufs- und Privatleben."},
            {"speaker": "Professor Weber", "text": "Zudem müssen sich Arbeitnehmer kontinuierlich weiterbilden, um mit dem rasanten technologischen Fortschritt Schritt halten zu können. Die Halbwertszeit von Wissen wird immer kürzer."},
            {"speaker": "Professor Weber", "text": "Es ist daher unerlässlich, dass sowohl Arbeitgeber als auch Arbeitnehmer proaktiv Strategien entwickeln, um mit diesen Veränderungen umzugehen, ohne dabei die mentale Gesundheit zu vernachlässigen."},
        ],
        "questions": [
            {"id": 1, "type": "fill_blank", "question": "Die ___ hat unsere Arbeitswelt grundlegend transformiert.", "answer": "Digitalisierung"},
            {"id": 2, "type": "fill_blank", "question": "Früher war die ___ am Arbeitsplatz obligatorisch.", "answer": "Präsenz"},
            {"id": 3, "type": "fill_blank", "question": "Die ständige Erreichbarkeit führt zu einer Verschwimmung der Grenze zwischen Berufs- und ___.", "answer": "Privatleben"},
            {"id": 4, "type": "fill_blank", "question": "Die ___ von Wissen wird immer kürzer.", "answer": "Halbwertszeit"},
            {"id": 5, "type": "fill_blank", "question": "Arbeitgeber und Arbeitnehmer müssen ___ Strategien entwickeln.", "answer": "proaktiv"},
        ],
    },

    # ---------- C1 · 解答题 · 气候政策 ----------
    {
        "title": "Klimapolitik im Wandel",
        "description": "Eine Diskussion über internationale Klimaschutzmaßnahmen.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Dr. Fischer", "gender": "female"},
            {"name": "Professor Schmidt", "gender": "male"},
        ],
        "text_segments": [
            {"speaker": "Dr. Fischer", "text": "Herr Professor Schmidt, die internationalen Klimagipfel der vergangenen Jahre haben trotz vielversprechender Ankündigungen kaum greifbare Ergebnisse geliefert. Wie erklären Sie sich diese Diskrepanz zwischen rhetorischem Anspruch und faktischem Handeln?"},
            {"speaker": "Professor Schmidt", "text": "Die Ursachen dafür sind zweifellos komplex. Einerseits existieren auf nationaler Ebene durchaus ambitionierte Klimaschutzziele, andererseits scheitern diese nicht selten an der mangelnden Umsetzungsbereitschaft der einzelnen Akteure, insbesondere wenn kurzfristige wirtschaftliche Interessen berührt werden."},
            {"speaker": "Dr. Fischer", "text": "Heißt das, dass die politischen Bekenntnisse letztlich nur symbolischen Charakter haben?"},
            {"speaker": "Professor Schmidt", "text": "Das wäre zu pauschal formuliert. Fakt ist jedoch, dass viele Staaten ihre zugesagten Emissionsreduktionen verfehlen, ohne dass dies nennenswerte Sanktionen nach sich ziehen würde. Das Pariser Abkommen beispielsweise entbehrt jeglicher verbindlichen Durchsetzungsmechanismen."},
            {"speaker": "Dr. Fischer", "text": "Welche Instrumente halten Sie denn für geeignet, um diesen Vollzugsdefizit zu beheben?"},
            {"speaker": "Professor Schmidt", "text": "Ich plädiere für die Einführung grenzüberschreitender CO2-Abgaben, die einen finanziellen Anreiz schaffen würden, ohne dabei die wirtschaftliche Wettbewerbsfähigkeit zu stark zu beeinträchtigen. Zudem sollten nicht nachhaltige Subventionen konsequent abgebaut werden."},
            {"speaker": "Dr. Fischer", "text": "Halten Sie es für realistisch, dass sich eine solche internationale Einigung in absehbarer Zeit verwirklichen lässt?"},
            {"speaker": "Professor Schmidt", "text": "Realistisch vielleicht nicht, aber zwingend notwendig zweifellos. Der Klimawandel wartet nicht auf politische Kompromisse."},
        ],
        "questions": [
            {"id": 1, "type": "open_ended", "question": "Welche Diskrepanz kritisiert Dr. Fischer zu Beginn?", "answer": "Die Diskrepanz zwischen rhetorischem Anspruch und faktischem Handeln bei internationalen Klimagipfeln."},
            {"id": 2, "type": "open_ended", "question": "Woran scheitern ambitionierte Klimaschutzziele laut Professor Schmidt?", "answer": "An der mangelnden Umsetzungsbereitschaft der einzelnen Akteure, insbesondere wenn kurzfristige wirtschaftliche Interessen berührt werden."},
            {"id": 3, "type": "open_ended", "question": "Welches Problem des Pariser Abkommens nennt Professor Schmidt?", "answer": "Das Abkommen entbehrt jeglicher verbindlichen Durchsetzungsmechanismen, sodass verfehlte Emissionsreduktionen keine Sanktionen nach sich ziehen."},
            {"id": 4, "type": "open_ended", "question": "Welches Instrument schlägt Professor Schmidt vor?", "answer": "Grenzüberschreitende CO2-Abgaben, die einen finanziellen Anreiz schaffen, sowie der konsequente Abbau nicht nachhaltiger Subventionen."},
            {"id": 5, "type": "open_ended", "question": "Wie bewertet Professor Schmidt die Realisierbarkeit seiner Vorschläge?", "answer": "Er hält sie vielleicht nicht für realistisch, aber für zwingend notwendig, da der Klimawandel nicht auf politische Kompromisse wartet."},
        ],
    },

    # ==================== C2 ====================

    # ---------- C2 · 选择题 · 哲学 ----------
    {
        "title": "Der Sinn des Lebens",
        "description": "Ein philosophisches Gespräch über die Suche nach Lebenssinn.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Dr. Schneider", "gender": "female"},
            {"name": "Professor Klein", "gender": "male"},
        ],
        "text_segments": [
            {"speaker": "Dr. Schneider", "text": "Herr Kollege, die Frage nach dem Sinn des Lebens beschäftigt die Philosophie seit Jahrtausenden. Wäre es nicht an der Zeit, diese Frage als obsolet zu betrachten?"},
            {"speaker": "Professor Klein", "text": "Ich würde widersprechen wollen. Gerade in einer zunehmend säkularisierten Gesellschaft, in der traditionelle Sinnsysteme an Erklärungskraft eingebüßt haben, gewinnt diese Frage eine unverminderte, ja geradezu gesteigerte Dringlichkeit."},
            {"speaker": "Dr. Schneider", "text": "Aber ist nicht gerade die Endlosigkeit dieser Debatte ein Indiz dafür, dass es keine universelle Antwort geben kann? Jede Epoche hat ihre eigenen Antworten hervorgebracht, die sich im Nachhinein als zeitgebunden erwiesen haben."},
            {"speaker": "Professor Klein", "text": "Das mag zwar zutreffen, doch würde ich argumentieren, dass nicht die Antworten selbst von Belang sind, sondern der Prozess der Reflexion. Die Frage nach dem Sinn ist gewissermaßen ein Katalysator für die intellektuelle und moralische Entwicklung des Individuums."},
            {"speaker": "Dr. Schneider", "text": "Das ist ein interessanter Gesichtspunkt. Aber birgt nicht gerade die ständige Beschäftigung mit dieser Frage die Gefahr, dass man das eigentliche Leben verpasst? Man könnte sagen, die Suche nach dem Sinn wird zur Vermeidungsstrategie."},
            {"speaker": "Professor Klein", "text": "Hier liegt m.E. ein wesentlicher Unterschied zwischen kontemplativer Philosophie und existenzieller Verfallenheit. Letztere wäre in der Tat problematisch, doch erstere befähigt uns gerade dazu, ein authentisches und selbstreflexives Leben zu führen."},
        ],
        "questions": [
            {"id": 1, "type": "multiple_choice", "question": "Welche These vertritt Dr. Schneider zu Beginn?",
             "options": ["A. Die Sinnfrage ist die wichtigste philosophische Frage",
                         "B. Die Frage nach dem Sinn des Lebens könnte als obsolet betrachtet werden",
                         "C. Es gibt eine universelle Antwort auf die Sinnfrage",
                         "D. Die Philosophie hat das Problem bereits gelöst"], "answer": "B"},
            {"id": 2, "type": "multiple_choice", "question": "Warum hält Professor Klein die Frage nach dem Lebenssinn für aktuell?",
             "options": ["A. Weil die Wissenschaft neue Erkenntnisse liefert",
                         "B. Weil die Regierung es fordert",
                         "C. Weil in einer säkularisierten Gesellschaft traditionelle Sinnsysteme an Erklärungskraft verloren haben",
                         "D. Weil es eine Modeerscheinung ist"], "answer": "C"},
            {"id": 3, "type": "multiple_choice", "question": "Welchen Wert misst Professor Klein dem Reflexionsprozess bei?",
             "options": ["A. Er ist irrelevant", "B. Er ist ein Katalysator für die intellektuelle und moralische Entwicklung",
                         "C. Er verhindert das eigentliche Leben", "D. Er führt zu Vermeidungsstrategien"], "answer": "B"},
            {"id": 4, "type": "multiple_choice", "question": "Welche Gefahr sieht Dr. Schneider in der ständigen Beschäftigung mit der Sinnfrage?",
             "options": ["A. Finanzieller Ruin", "B. Soziale Isolation",
                         "C. Die Suche wird zur Vermeidungsstrategie und man verpasst das eigentliche Leben", "D. Beruflicher Misserfolg"], "answer": "C"},
            {"id": 5, "type": "multiple_choice", "question": "Welchen Unterschied betont Professor Klein am Schluss?",
             "options": ["A. Zwischen Theorie und Praxis", "B. Zwischen kontemplativer Philosophie und existenzieller Verfallenheit",
                         "C. Zwischen östlicher und westlicher Philosophie", "D. Zwischen Akademikern und Laien"], "answer": "B"},
        ],
    },

    # ---------- C2 · 填空题 · 文学分析 ----------
    {
        "title": "Literarische Interpretation",
        "description": "Ein Seminar über die Interpretation moderner Literatur.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Professor Mann", "gender": "male"},
            {"name": "Clara", "gender": "female"},
        ],
        "text_segments": [
            {"speaker": "Professor Mann", "text": "Die Frage, ob der Autorintention bei der Interpretation literarischer Werke eine maßgebliche Bedeutung zukommt, hat die Literaturwissenschaft seit jeher beschäftigt und entbehrt nicht einer gewissen Ironie."},
            {"speaker": "Clara", "text": "Wenn ich Sie richtig verstehe, spielen Sie darauf an, dass die Intention des Autors häufig rekonstruiert wird, obwohl sie einer empirischen Überprüfung im strengen Sinne nicht zugänglich ist?"},
            {"speaker": "Professor Mann", "text": "Präzise formuliert. Die Autorintention wird gewissermaßen zu einer Fiktion, die der Interpret konstruiert, um dem Text einen kohärenten Sinn zu verleihen."},
            {"speaker": "Clara", "text": "Wäre dann nicht der Tod des Autors, wie Barthes es formulierte, die konsequenteste Position?"},
            {"speaker": "Professor Mann", "text": "Das ist eine zulässige Schlussfolgerung, obgleich sie m.E. das Kind mit dem Bade ausschüttet. Die vollständige Negation der Autorintention birgt die Gefahr einer beliebigen Interpretation, die den Text seiner Spezifität beraubt."},
        ],
        "questions": [
            {"id": 1, "type": "fill_blank", "question": "Die ___ des Autors ist einer empirischen Überprüfung nicht zugänglich.", "answer": "Intention"},
            {"id": 2, "type": "fill_blank", "question": "Die Autorintention wird zu einer ___, die der Interpret konstruiert.", "answer": "Fiktion"},
            {"id": 3, "type": "fill_blank", "question": "Barthes formulierte den Tod des ___.", "answer": "Autors"},
            {"id": 4, "type": "fill_blank", "question": "Die vollständige Negation birgt die Gefahr einer ___ Interpretation.", "answer": "beliebigen"},
            {"id": 5, "type": "fill_blank", "question": "Sie beraubt den Text seiner ___.", "answer": "Spezifität"},
        ],
    },

    # ---------- C2 · 解答题 · 哲学思辨 ----------
    {
        "title": "Der Sinn des Lebens (Diskussion)",
        "description": "Ein philosophisches Gespräch über die Suche nach Lebenssinn.",
        "text_type": "dialogue",
        "speakers": [
            {"name": "Dr. Schneider", "gender": "female"},
            {"name": "Professor Klein", "gender": "male"},
        ],
        "text_segments": [
            {"speaker": "Dr. Schneider", "text": "Herr Kollege, die Frage nach dem Sinn des Lebens beschäftigt die Philosophie seit Jahrtausenden. Wäre es nicht an der Zeit, diese Frage als obsolet zu betrachten?"},
            {"speaker": "Professor Klein", "text": "Ich würde widersprechen wollen. Gerade in einer zunehmend säkularisierten Gesellschaft, in der traditionelle Sinnsysteme an Erklärungskraft eingebüßt haben, gewinnt diese Frage eine unverminderte, ja geradezu gesteigerte Dringlichkeit."},
            {"speaker": "Dr. Schneider", "text": "Aber ist nicht gerade die Endlosigkeit dieser Debatte ein Indiz dafür, dass es keine universelle Antwort geben kann? Jede Epoche hat ihre eigenen Antworten hervorgebracht, die sich im Nachhinein als zeitgebunden erwiesen haben."},
            {"speaker": "Professor Klein", "text": "Das mag zwar zutreffen, doch würde ich argumentieren, dass nicht die Antworten selbst von Belang sind, sondern der Prozess der Reflexion. Die Frage nach dem Sinn ist gewissermaßen ein Katalysator für die intellektuelle und moralische Entwicklung des Individuums."},
            {"speaker": "Dr. Schneider", "text": "Das ist ein interessanter Gesichtspunkt. Aber birgt nicht gerade die ständige Beschäftigung mit dieser Frage die Gefahr, dass man das eigentliche Leben verpasst? Man könnte sagen, die Suche nach dem Sinn wird zur Vermeidungsstrategie."},
            {"speaker": "Professor Klein", "text": "Hier liegt m.E. ein wesentlicher Unterschied zwischen kontemplativer Philosophie und existenzieller Verfallenheit. Letztere wäre in der Tat problematisch, doch erstere befähigt uns gerade dazu, ein authentisches und selbstreflexives Leben zu führen."},
        ],
        "questions": [
            {"id": 1, "type": "open_ended", "question": "Welche These vertritt Dr. Schneider zu Beginn des Gesprächs?", "answer": "Sie schlägt vor, die Frage nach dem Sinn des Lebens als obsolet zu betrachten."},
            {"id": 2, "type": "open_ended", "question": "Warum hält Professor Klein die Frage nach dem Lebenssinn für aktuell?", "answer": "In einer säkularisierten Gesellschaft, in der traditionelle Sinnsysteme an Erklärungskraft verloren haben, gewinnt die Frage an Dringlichkeit."},
            {"id": 3, "type": "open_ended", "question": "Welches Argument führt Dr. Schneider gegen die Universalität der Antwort an?", "answer": "Jede Epoche hat ihre eigenen Antworten hervorgebracht, die sich als zeitgebunden erwiesen haben, was gegen eine universelle Antwort spricht."},
            {"id": 4, "type": "open_ended", "question": "Welchen Wert misst Professor Klein dem Prozess der Reflexion bei?", "answer": "Nicht die Antworten selbst sind von Belang, sondern der Prozess der Reflexion, der als Katalysator für die intellektuelle und moralische Entwicklung des Individuums dient."},
            {"id": 5, "type": "open_ended", "question": "Welche Gefahr sieht Dr. Schneider in der ständigen Beschäftigung mit der Sinnfrage?", "answer": "Die Suche nach dem Sinn könnte zur Vermeidungsstrategie werden, bei der man das eigentliche Leben verpasst."},
        ],
    },
]


def get_demo_content(difficulty: str, question_type: str, theme: str) -> dict | None:
    """
    获取匹配的 Demo 内容。
    优先精确匹配等级+题型，其次匹配等级，最后匹配题型。
    """
    # 精确匹配等级和题型
    for ex in DEMO_EXERCISES:
        ex_level = _infer_level(ex)
        ex_qtype = _infer_qtype(ex)
        if ex_level == difficulty and ex_qtype == question_type:
            return ex

    # 匹配等级
    for ex in DEMO_EXERCISES:
        if _infer_level(ex) == difficulty:
            return ex

    # 匹配题型
    for ex in DEMO_EXERCISES:
        if _infer_qtype(ex) == question_type:
            return ex

    # 随机返回
    if DEMO_EXERCISES:
        import random
        return random.choice(DEMO_EXERCISES)

    return None


def _infer_level(exercise: dict) -> str:
    """从练习内容推断 CEFR 等级"""
    title = exercise.get("title", "")
    level_map = {
        "Begrüßung": "A1", "Restaurant": "A1", "Mein Tag": "A1",
        "Freizeit": "A2", "Einkaufen": "A2", "Urlaub": "A2",
        "Bewerbung": "B1", "Reise nach München": "B1", "Mülltrennung": "B1",
        "Umweltschutz": "B2", "Arbeitswelt": "B2", "Bildungssystem": "B2",
        "Digitalisierung": "C1", "Zukunft der Arbeitswelt": "C1", "Klimapolitik": "C1",
        "Sinn des Lebens": "C2", "Literarische": "C2",
    }
    for keyword, level in level_map.items():
        if keyword.lower() in title.lower():
            return level
    return "A1"


def _infer_qtype(exercise: dict) -> str:
    """从练习内容推断题型"""
    questions = exercise.get("questions", [])
    if not questions:
        return "选择题"
    qtype = questions[0].get("type", "")
    type_map = {
        "multiple_choice": "选择题",
        "fill_blank": "填空题",
        "open_ended": "解答题",
    }
    return type_map.get(qtype, "选择题")
