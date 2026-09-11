# Concept definitions. Each: id, ar (Arabic label), en, root(s), polarity ('virtue'|'haram'), category, lemmas (as spelled in the morphology lemma list), opposite (id), key (surah:ayah)
# polarity 'haram' = forbidden / condemned in the text. 'virtue' = commanded / praised.
CATEGORIES = {
    'belief':  {'ar': 'العقيدة', 'en': 'Belief & the heart'},
    'worship': {'ar': 'العبادات', 'en': 'Worship'},
    'character': {'ar': 'الأخلاق', 'en': 'Character'},
    'speech':  {'ar': 'اللسان', 'en': 'The tongue'},
    'money':   {'ar': 'المال', 'en': 'Money & dealings'},
    'family':  {'ar': 'الأسرة والجنس', 'en': 'Family & sex'},
    'food':    {'ar': 'الطعام والشراب', 'en': 'Food & drink'},
    'blood':   {'ar': 'الدم والعدوان', 'en': 'Blood, war & aggression'},
}

C = []
def c(id, ar, en, root, pol, cat, lemmas, opposite=None, key=None, note=None, refs=None):
    C.append(dict(id=id, ar=ar, en=en, root=root, pol=pol, cat=cat, lemmas=lemmas, opposite=opposite, key=key, note=note, refs=refs or []))

# ---------- BELIEF ----------
c('iman','الإيمان','Faith','ء-م-ن','virtue','belief',['ءامن','مءمن'],'kufr','2:285')
c('kufr','الكفر','Disbelief / ingratitude','ك-ف-ر','haram','belief',['كفر','كافر'],'iman','2:6', 'Root also carries "ingratitude" (kufr al-ni\'ma); the text does not separate the two.')
c('shirk','الشرك','Associating partners with God','ش-ر-ك','haram','belief',['اشرك','مشرك','شريك','شرك'],'ibadah','4:48','The one sin the text says God does not forgive (4:48, 4:116).')
c('ibadah','العبادة (التوحيد)','Worship of God alone','ع-ب-د','virtue','belief',['عبد','عابد'],'shirk','51:56')
c('taqwa','التقوى','God-consciousness','و-ق-ي','virtue','belief',['اتقي', 'تقوي', 'متقين'],None,'49:13')
c('nifaq','النفاق','Hypocrisy','ن-ف-ق','haram','belief',['منفقون', 'منفقت', 'منفقين', 'نفاق'],'ikhlas','4:145')
c('ikhlas','الإخلاص','Sincerity to God','خ-ل-ص','virtue','belief',['مخلص','اخلص'],'nifaq','98:5')
c('tawakkul','التوكل','Reliance on God','و-ك-ل','virtue','belief',['توكل', 'متوكلون'],None,'65:3')
c('sabr','الصبر','Patience / steadfastness','ص-ب-ر','virtue','character',['صبر','صابر','صبار'],None,'2:153')
c('shukr','الشكر','Gratitude','ش-ك-ر','virtue','belief',['شكر','شاكر','شكور'],'kufr','14:7')
c('tawba','التوبة','Repentance','ت-و-ب','virtue','belief',['تاب','توبة','تواب'],None,'66:8')
c('khashya','الخشية / الخوف من الله','Fear / awe of God','خ-ش-ي','virtue','belief',['خشي','خشية'],None,'35:28')
c('dhikr','ذكر الله','Remembrance of God','ذ-ك-ر','virtue','worship',['ذكر'],'ghafla','33:41','Lemma ذكر also covers "the Reminder" (the Quran itself) and "mention" — counted as is.')
c('sihr','السحر','Magic / sorcery','س-ح-ر','haram','belief',['سحر', 'سحار', 'مسحرين'],None,'2:102')
c('ridda','الردة','Apostasy','ر-د-د','haram','belief',['ارتد'],None,'2:217')
c('yaqin','اليقين','Certainty','ي-ق-ن','virtue','belief',['يقين', 'استيقنت', 'مستيقنين', 'موقنين'],'zann','2:4')
c('qunut','القنوت','Devout obedience','ق-ن-ت','virtue','worship',['قانت', 'قنتت', 'يقنت'],None,'33:35')

# ---------- WORSHIP ----------
c('salah','الصلاة','Prayer','ص-ل-و','virtue','worship',['صلوة','صلي','مصلي'],None,'2:43')
c('zakah','الزكاة','Obligatory alms','ز-ك-و','virtue','worship',['زكوة'],None,'2:43','The verb زكّى (to purify) is excluded; only the noun الزكاة is counted.')
c('sawm','الصيام','Fasting','ص-و-م','virtue','worship',['صيام', 'صوم'],None,'2:183')
c('hajj','الحج','Pilgrimage','ح-ج-ج','virtue','worship',['حج','عمرة'],None,'3:97')
c('dua','الدعاء','Supplication','د-ع-و','virtue','worship',['دعا','دعاء'],None,'40:60','Lemma دعا also means "to call / invite" (incl. calling on idols) — counted as is.')
c('sujud','السجود والركوع','Prostration & bowing','س-ج-د','virtue','worship',['سجد', 'ساجد', 'سجود', 'يركع', 'راكع'],None,'22:77')
c('tilawa','تلاوة القرآن','Reciting the Quran','ت-ل-و','virtue','worship',['تلي'],None,'73:4')
c('jihad','الجهاد في سبيل الله','Striving in God\'s cause','ج-ه-د','virtue','blood',['جهد', 'جهاد', 'مجهدين'],None,'9:20','Includes both armed and non-armed striving; the text uses one word.')
c('nadhr','الوفاء بالنذر','Fulfilling vows','ن-ذ-ر','virtue','worship',['نذر'],None,'76:7','Only the noun/verb "vow" — the far more common نذير (warner) is excluded.')

# ---------- CHARACTER ----------
c('ihsan','الإحسان','Excellence / doing good','ح-س-ن','virtue','character',['احسن', 'محسن', 'حسنة'],'isaa','16:90')
c('adl','العدل والقسط','Justice','ع-د-ل / ق-س-ط','virtue','character',['عدل', 'قسط', 'اقسط', 'مقسطين', 'تقسط', 'قسطاس'],'zulm','4:58')
c('zulm','الظلم','Wrongdoing / injustice','ظ-ل-م','haram','character',['ظلم','ظالم','ظلوم'],'adl','42:40')
c('afw','العفو والصفح','Pardon & forgiveness of others','ع-ف-و','virtue','character',['عفا', 'عفو', 'يصفح', 'صفح'],None,'42:40')
c('rahma','الرحمة','Mercy / compassion','ر-ح-م','virtue','character',['رحم', 'رحمة', 'مرحمة', 'ارحم', 'رحمين'],None,'90:17','The divine names الرحمن / الرحيم are excluded; رحمة itself is still mostly God\'s mercy, counted as is.')
c('kibr','الكبر والاستكبار','Arrogance','ك-ب-ر','haram','character',['استكبر','مستكبر','كبر','مختال','فخور','متكبر'],'tawadu','31:18')
c('tawadu','التواضع والخشوع','Humility','خ-ش-ع / ه-و-ن','virtue','character',['خاشع', 'خشوع', 'خشعت', 'هون'],'kibr','25:63')
c('baghy','البغي','Oppression / transgression','ب-غ-ي','haram','character',['بغي','باغ'],None,'42:42','Lemma بغي also = "to seek" (ابتغى is separate). Counted as is.')
c('hasad','الحسد','Envy','ح-س-د','haram','character',['حسد','حاسد'],None,'113:5')
c('ghadab','الغضب','Anger','غ-ض-ب','haram','character',['غضب', 'غضبن', 'مغضوب'],'kazm','42:37','Mostly God\'s anger against wrongdoers; human anger is condemned in 42:37 and 3:134.')
c('kazm','كظم الغيظ والحلم','Restraining anger / forbearance','ك-ظ-م / ح-ل-م','virtue','character',['كظمين', 'حليم'],'ghadab','3:134')
c('amana','الأمانة','Trustworthiness','ء-م-ن','virtue','character',['امنت', 'امين', 'امنة'],'khiyana','4:58')
c('khiyana','الخيانة','Betrayal / treachery','خ-و-ن','haram','character',['خان', 'خاءنين', 'خاءنة', 'خيانة', 'خوان'],'amana','8:27')
c('wafa','الوفاء بالعهد','Keeping promises & covenants','و-ف-ي / ع-ه-د','virtue','character',['اوفي','عهد','ميثق'],None,'17:34')
c('haya','العفة وحفظ الفرج','Chastity / guarding modesty','ع-ف-ف / ح-ف-ظ','virtue','family',['يستعفف', 'تعفف', 'حفظ', 'فرج', 'يغض', 'محصنت', 'احصنت', 'محصنة'],'zina','24:30')
c('israf','الإسراف والتبذير','Extravagance / waste','س-ر-ف / ب-ذ-ر','haram','money',['اسرف', 'مسرف', 'تبذر', 'مبذرين'],None,'17:27')
c('sukhriya','السخرية والاستهزاء','Mockery','س-خ-ر / ه-ز-ء','haram','speech',['سخر', 'هزو', 'استهزء', 'مستهزءون', 'سخري'],None,'49:11')
c('ghurur','الغرور والفرح بالدنيا','Delusion / vain pride','غ-ر-ر / ف-ر-ح','haram','character',['غرور','غر','فرح','مرح'],None,'57:20')
c('lahw','اللهو واللعب','Idle diversion','ل-ه-و / ل-ع-ب','haram','character',['لهو','لعب','لاهية','الهي'],None,'62:11')
c('salih','العمل الصالح والإصلاح','Righteous deeds & reconciliation','ص-ل-ح','virtue','character',['صلحت', 'صلح', 'اصلح', 'مصلح'],'fasad','103:3')
c('fasad','الفساد في الأرض','Corruption on earth','ف-س-د','haram','blood',['فساد', 'مفسد', 'افسد', 'فسدت'],'salih','2:205')
c('fisq','الفسق','Defiant sin','ف-س-ق','haram','character',['فسق','فاسق','فسوق'],None,'49:7')
c('ithm','الإثم والذنوب','Sin (general)','ء-ث-م / ذ-ن-ب','haram','character',['اثم', 'اثيم', 'ذنب'],None,'7:33')
c('birr','البر','Righteousness / piety','ب-ر-ر','virtue','character',['بر'],None,'2:177')
c('nasiha','النصيحة والموعظة','Sincere advice & admonition','ن-ص-ح / و-ع-ظ','virtue','speech',['نصح','ناصح','موعظة','وعظ'],None,'31:13')
c('maruf','الأمر بالمعروف والنهي عن المنكر','Enjoining right, forbidding wrong','ع-ر-ف / ن-ك-ر','virtue','character',['معروف','منكر'],None,'3:104')
c('taawun','التعاون والأخوة','Cooperation & brotherhood','ع-و-ن / ء-خ-و','virtue','character',['تعاون', 'اخوة'],None,'5:2','إخوة also covers Joseph\'s brothers etc. Counted as is.')
c('ilm','التفكر والتعقل والتدبر','Reflection & using reason','ف-ك-ر / ع-ق-ل / د-ب-ر','virtue','character',['يتفكر', 'يتدبر', 'عقل'],None,'39:9',None)

# ---------- SPEECH ----------
c('sidq','الصدق','Truthfulness','ص-د-ق','virtue','speech',['صدق','صادق','صديق','صدق'],'kadhib','9:119')
c('kadhib','الكذب','Lying / denial','ك-ذ-ب','haram','speech',['كذب', 'كذاب', 'مكذبين'],'sidq','16:105','Includes takdhīb — denying God\'s revelation — which is most of the count.')
c('iftira','الافتراء والبهتان','Fabrication & slander','ف-ر-ي / ب-ه-ت','haram','speech',['افتري','بهتن','مفتر','زور'],None,'24:15')
c('shahada','الشهادة بالحق','Truthful testimony','ش-ه-د','virtue','speech',['شهد','شهدة','شهيد','شاهد'],'kitman','4:135')
c('kitman','كتمان الشهادة والحق','Concealing truth / testimony','ك-ت-م','haram','speech',['كتم'],'shahada','2:283')
c('laghw','اللغو والجدال','Idle talk & quarrelling','ل-غ-و / ج-د-ل','haram','speech',['لغو','جدال','جدل','خوض'],None,'23:3')
c('ghiba','الغيبة والتجسس والظن','Backbiting, spying, suspicion','غ-ي-ب / ج-س-س / ظ-ن-ن','haram','speech',['يغتب', 'تجسس', 'ظن'],'yaqin','49:12','ظنّ mostly means "to think/assume" — 49:12 forbids the sinful kind. Counted as is.')
c('lamz','اللمز والهمز والنميمة','Taunting, insulting, tale-bearing','ل-م-ز / ه-م-ز / ن-م-م','haram','speech',['يلمز', 'همزة', 'لمزة', 'همزت', 'نميم'],None,'104:1')
c('lan','اللعن والسب','Cursing & abuse','ل-ع-ن / س-ب-ب','haram','speech',['لعن', 'لعنة'],None,'6:108','Mostly God\'s curse on wrongdoers; cursing others\' gods is forbidden in 6:108.')
c('halif','الحلف وأيمان اللغو','Swearing false / idle oaths','ح-ل-ف / ي-م-ن','haram','speech',['حلف'],None,'2:224','Lemma حلف plus the oath verses using أيمان (which shares a spelling with faith and is not counted wholesale).', refs=['2:224','2:225','5:89','16:91','16:92','16:94','24:22','66:2','68:10','3:77'])
c('qawl_hasan','القول الحسن واللين','Kind & gentle speech','ق-و-ل','virtue','speech',['لين', 'لينة'],None,'2:83','No single word; the explicit commands about how to speak are listed.', refs=['2:83','2:263','4:5','4:8','4:9','17:23','17:28','17:53','20:44','33:32','33:70','41:33','41:34','29:46','16:125','25:63'])

# ---------- MONEY ----------
c('infaq','الإنفاق في سبيل الله','Spending in God\'s cause','ن-ف-ق','virtue','money',['انفق', 'نفقة', 'نفقت'],'bukhl','2:261')
c('sadaqa','الصدقة والقرض الحسن','Charity & goodly loans','ص-د-ق / ق-ر-ض','virtue','money',['صدقة','صدقت','قرض','تصدق','مصدق'],None,'2:271')
c('riba','الربا','Usury / interest','ر-ب-و','haram','money',['ربوا'],'sadaqa','2:275','Root ر-ب-و also = "to grow"; only the noun الربا is counted.', refs=['30:39','2:279'])
c('bukhl','البخل والشح','Miserliness','ب-خ-ل / ش-ح-ح','haram','money',['بخل', 'شح'],'infaq','3:180')
c('kanz','كنز المال','Hoarding wealth','ك-ن-ز','haram','money',['كنز'],'infaq','9:34')
c('yatim','رعاية اليتيم والمسكين','Care for orphans & the poor','ي-ت-م / س-ك-ن / ف-ق-ر','virtue','money',['يتيم','مسكين','فقير','مسكين','ساءل','محروم'],None,'93:9')
c('kayl','الوفاء بالكيل والميزان','Honest weights & measures','ك-ي-ل / و-ز-ن','virtue','money',['كيل', 'ميزان', 'وزن', 'مكيال', 'مطففين'],None,'83:1')
c('suht','السحت وأكل المال بالباطل','Unlawful gain / devouring wealth wrongly','س-ح-ت / ب-ط-ل','haram','money',['سحت'],'kayl','4:29','سحت plus the verses about consuming wealth بالباطل.', refs=['2:188','4:29','4:161','9:34','2:275'])
c('rishwa','الرشوة','Bribery','د-ل-و','haram','money',['ادلي'],None,'2:188','Only one verse (2:188: "…and hand it over to judges"). No dedicated word.')
c('maysir','الميسر (القمار)','Gambling','ي-س-ر','haram','food',['ميسر'],None,'5:90')
c('tijara','التجارة والبيع الحلال','Lawful trade','ت-ج-ر / ب-ي-ع','virtue','money',['تجرة','بيع','تاجر'],'riba','2:275')
c('dayn','كتابة الدين والرهن','Recording debts','د-ي-ن / ر-ه-ن','virtue','money',['رهن'],None,'2:282')

# ---------- FAMILY & SEX ----------
c('walidayn','بر الوالدين','Kindness to parents','و-ل-د','virtue','family',['والد', 'ابوان'],'uquq','17:23',None)
c('uquq','عقوق الوالدين','Disrespecting parents','ء-ف-ف','haram','family',['اف'],'walidayn','17:23','No dedicated word; the Quran forbids even saying "uff" to them (17:23).')
c('rahim','صلة الرحم والقربى','Kinship ties & relatives','ر-ح-م / ق-ر-ب','virtue','family',['ارحام','قربي'],'qatia','4:1')
c('qatia','قطيعة الرحم','Severing kinship','ق-ط-ع','haram','family',[],'rahim','47:22','No dedicated word; the verses that condemn cutting kinship are listed.', refs=['2:27','13:25','47:22','4:1'])
c('zina','الزنا','Fornication / adultery','ز-ن-ي','haram','family',['زان', 'زانية', 'زني'],'haya','17:32', refs=['25:68','60:12','24:2','4:15','4:16','4:25'])
c('liwat','فاحشة قوم لوط','The act of Lot\'s people (male-male sex)','ل-و-ط','haram','family',['لوط'],None,'7:81','Counted via the name لوط; the act is described in 7:80-81, 26:165-166, 27:55, 29:28-29.')
c('fahisha','الفاحشة','Gross indecency','ف-ح-ش','haram','family',['فحشة', 'فحشاء'],None,'6:151')
c('qadhf','قذف المحصنات','Accusing chaste women','ر-م-ي','haram','family',[],None,'24:4','The accusation verses of Surat an-Nur, listed explicitly.', refs=['24:4','24:5','24:6','24:23','24:11','24:12','24:13','24:15','24:16','24:19'])
c('nikah','النكاح','Marriage','ن-ك-ح / ز-و-ج','virtue','family',['نكح','نكاح','زوج','زوجت','تنكح'],'zina','24:32')
c('talaq','الطلاق (بالمعروف)','Divorce (with decency)','ط-ل-ق','virtue','family',['طلق', 'مطلقت'],None,'65:1','Permitted, regulated, not praised — listed under virtues only because the text commands doing it decently.')
c('hijab','الحجاب وغض البصر','Covering & lowering the gaze','ح-ج-ب / خ-م-ر','virtue','family',['حجاب','خمر','جلبيب','يغض','زينة'],None,'24:31','خمر here = head-covering (خُمُر); the same lemma spelling as wine in this dataset, so both are counted — see 5:90 vs 24:31.')
c('jar','الإحسان إلى الجار والضيف','Kindness to neighbours & guests','ج-و-ر / ض-ي-ف','virtue','family',['جار','ضيف'],None,'4:36')

# ---------- FOOD & DRINK ----------
c('khamr','الخمر','Wine / intoxicants','خ-م-ر','haram','food',['خمر', 'سكري', 'سكرة', 'سكر'],'tayyibat','5:90','Shares lemma spelling with خُمُر (head-coverings) in 24:31 — that verse is included; the text itself distinguishes them.')
c('mayta','الميتة والدم ولحم الخنزير','Carrion, blood, pork','م-و-ت / د-م-و / خ-ن-ز-ر','haram','food',['ميتة','دم','خنزير'],'tayyibat','2:173','دم also appears in narrative (blood of Egypt\'s plague, etc.). Counted as is.')
c('ansab','الأنصاب والأزلام','Sacrificial stones & divining arrows','ن-ص-ب / ز-ل-م','haram','food',['نصب', 'ازلم'],None,'5:3')
c('ghayr_allah','ما أُهِلَّ لغير الله','Meat dedicated to other than God','ه-ل-ل','haram','food',[],None,'2:173','No dedicated word; the five verses that state it are listed explicitly.', refs=['2:173','5:3','6:121','6:145','16:115'])
c('tayyibat','الطيبات والحلال','Good, lawful things','ط-ي-ب / ح-ل-ل','virtue','food',['طيبت', 'طيب', 'حلل', 'احل', 'حل'],'haram_w','2:168')
c('haram_w','الحرام (التحريم)','What is made forbidden','ح-ر-م','haram','food',['حرام','حرم','محرم','حرمت'],'tayyibat','5:3','The umbrella word itself — every verse where the text says something is ḥarām or muḥarram.')
c('sayd','الصيد والذبح والإحرام','Hunting, slaughter & pilgrim state','ص-ي-د / ذ-ب-ح','virtue','food',['صيد', 'ذبح', 'انحر'],None,'5:96',None)

# ---------- BLOOD & AGGRESSION ----------
c('qatl','القتل','Killing / fighting','ق-ت-ل','haram','blood',['قتل', 'قتال'],'qisas','5:32','One lemma covers murder (4:93), fighting in war (2:190), and killing of prophets. Counted as is.')
c('qisas','القصاص والدية','Retaliation & blood-money','ق-ص-ص','virtue','blood',['قصاص','دية'],'qatl','2:178','Law, not virtue — placed here as the sanctioned answer to killing.')
c('itida','الاعتداء والعدوان','Aggression / transgressing limits','ع-د-و','haram','blood',['اعتدي','معتد','عدون','عدو'],'salam','2:190','Lemma عدو also = "enemy". Counted as is.')
c('sariqa','السرقة','Theft','س-ر-ق','haram','money',['سرق','سارق'],None,'5:38')
c('salam','السلم والصلح','Peace & making peace','س-ل-م','virtue','blood',['سلم', 'صلح', 'اصلح'],'itida','8:61')
c('nasr','نصرة المظلوم والمستضعف','Aiding the oppressed','ن-ص-ر / ض-ع-ف','virtue','blood',['نصر', 'مستضعفون', 'استضعف'],None,'4:75','Lemma نصر mostly = God\'s help/victory. Counted as is.')
c('tughyan','الطغيان','Tyranny','ط-غ-ي','haram','blood',['طغي', 'طغين', 'طاغية', 'طغوي', 'طغوت', 'اطغي'],None,'20:24')
c('fitna','الفتنة','Persecution / trial','ف-ت-ن','haram','blood',['فتنة','فتن'],None,'2:191','Fitna = both persecution and trial/test. Counted as is.')
