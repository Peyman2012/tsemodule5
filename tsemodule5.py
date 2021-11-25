"""
version 4.1
code by @Python4finance

Sample :
import tsemodule as tm
tm.stocklist()   #show all stock names
tm.stock(stock name,date range,get new file)
for example:
tm.stock("ABAD1",100,True)

"""
import pandas as pd
import io
import requests as rq

stocknames = {
"IKCQ1":"62616504891233280",
"NBAB1":"37661500521100963",
"APPE1":"55254206302462116",
"ASIA1":"51106317433079213",
"CONT1":"44834847569322522",
"CONX1":"57329318081089375",
"OPAL1":"655060129740445",
"ETKA1":"27405735172634593",
"ETKX1":"53295835881618508",
"ZBAL1":"51379017087081407",
"MKBT1":"22811176775480091",
"MKBX1":"45768538238520265",
"ARDS1":"35331248532537562",
"RVND1":"58356374066358100",
"ASTC1":"14079693677610396",
"OFOG1":"49502666250908008",
"OFOX1":"1911343624441437",
"BKLA1":"49869693814643443",
"ACTV1":"66991919802409760",
"BALB1":"70270965300262393",
"BABX1":"12231544096052404",
"OMID1":"18599703143458101",
"OMIX1":"45104299259467366",
"TSAN1":"58873907630765023",
"BENA1":"61725225143026283",
"BENB1":"16330743198286823",
"BENC1":"49641108336531623",
"BAKH1":"751415341879364",
"BAKX1":"46858597966426366",
"KALZ1":"62952165421099192",
"KALX1":"16471519272060905",
"KBLI1":"26711011601058186",
"KBLX1":"5857871270392801",
"TRNS1":"46752599569017089",
"TRNX1":"53697601723435147",
"KTAK1":"19734078707717188",
"KTAX1":"8823734825807435",
"JHRM1":"45118736321317244",
"TTZC1":"64703398743024121",
"BRKT1":"34557241988629814",
"BRKX1":"8981227815720204",
"SWIC1":"47377315952751604",
"SWIX1":"23484847504768205",
"LAPS1":"69454539056549106",
"LAPX1":"39023890840208765",
"BFJR1":"46178280540110577",
"BFJX1":"10741091548027385",
"JOSH1":"70219663893822560",
"JOSX1":"29195987083197059",
"KGND1":"22382156782768756",
"KGNX1":"65266756318187150",
"MOTJ1":"22086876724551482",
"MOTX1":"1931037287459558",
"NIRO1":"20453828618330936",
"NIRX1":"46629374720083542",
"BORS1":"60523145697836739",
"BONA1":"50247622569476338",
"ARTA1":"29242941150825379",
"ARTX1":"64910575313738889",
"PARS1":"6110133418282108",
"PASN1":"23441366113375722",
"PASX1":"36319830972593153",
"IPAR1":"9481703061634967",
"IPAX1":"50201903966895115",
"YASA1":"63580313877463104",
"YASX1":"32338211917133256",
"PASH1":"62786156501584862",
"PAHX1":"4208841225215712",
"TAIR1":"41935584690956944",
"TAIX1":"7503566413749235",
"IPTR1":"69143674941561637",
"IPTX1":"32874370564962210",
"DRKH1":"24079409192818584",
"DRKX1":"46023027311928862",
"DENA1":"58120226425289272",
"DENX1":"13119207966484500",
"PRKT1":"59607545337891226",
"PRKX1":"34432997122108874",
"AYEG1":"15039949673085566",
"AYEX1":"14819787164502995",
"PERS1":"10497143354080476",
"SHND1":"10120557300120078",
"SHNX1":"67337799462256399",
"SHIN1":"38196133309450513",
"SHIX1":"71208440662682926",
"BARZ1":"23214828924506640",
"BARX1":"8676363345079392",
"KVRZ1":"7235435095059069",
"KVRX1":"41228676018429540",
"LALZ1":"5208723461432451",
"LALX1":"41189775395878190",
"PLST1":"14419337127600051",
"PLSX1":"37494506460682322",
"PLKK1":"57722642338781674",
"PLKX1":"13778389952963406",
"GAZL1":"5938543336901420",
"GAZX1":"45851925911348490",
"LYZD1":"3681415009616010",
"PTAP1":"22560050433388046",
"PTAX1":"6491687805743913",
"SADR1":"23293437377896568",
"SDDX1":"35150770536114195",
"TRIR1":"19298748452450329",
"TRIX1":"69858202392669780",
"HPKO1":"6274378166234446",
"HPKX1":"44717433734548029",
"PIRN1":"43062880954780884",
"PIRX1":"47931755217693300",
"TDBR1":"7505613986635677",
"MOZI1":"8106875813689926",
"MOZX1":"70508258744702923",
"FROZ1":"60938976068667707",
"FROX1":"58999606802857888",
"TKLA1":"67612261115225625",
"GSKE1":"62258804563636993",
"GSKX1":"66191028275418950",
"COMB1":"30719054967088301",
"COMX1":"70480481633645190",
"TKNO1":"3654864906585643",
"TKNX1":"21727652065573865",
"MNMH1":"15826229869421585",
"MNMX1":"58349566728384453",
"TMDN1":"63679592178109910",
"TMLT1":"11129387075131725",
"TMLX1":"33666678504801754",
"TNOV1":"25357135030606405",
"TNOX1":"379466056274101",
"DTIP1":"29758477602878557",
"DTIX1":"43472427638799679",
"ABAD1":"59612098290740355",
"ABAX1":"34429961038727682",
"BSTE1":"17800036702302776",
"BSTX1":"68798377122760225",
"SAJN1":"22215980602177059",
"SAJX1":"26257365377629881",
"SESF1":"7424617629476020",
"SESX1":"22328556318373924",
"SGOS1":"66456062140680461",
"SGOX1":"50193280705263642",
"TOOM1":"18568733593280948",
"BEKA1":"14744445176220774",
"SAHD1":"63481599728522324",
"SAHX1":"28593434160948209",
"PMSZ1":"6043384171800349",
"PMSX1":"35030544513071961",
"OFRS1":"30852391633490755",
"OFRX1":"39191249877936167",
"MSKN1":"3863538898378476",
"MSKX1":"28570444064425663",
"BMLI1":"8403167990439117",
"NSTH1":"32845891587040106",
"NSTX1":"4325911723150569",
"PJMZ1":"32357363984168442",
"JPPC1":"27096851668435724",
"PJMX1":"39154317701922264",
"OFST1":"23936607891892333",
"OFSX1":"26972528518663385",
"BPRS1":"68102953053087817",
"BPRX1":"57715478894469223",
"CHDN1":"12329519546621752",
"FIBR1":"64358061873294912",
"FIBX1":"54424603805821073",
"KAPA1":"28957320033282870",
"KMSH1":"45709267601703167",
"KMSX1":"23525504731363137",
"KRTI1":"53113471126689455",
"KRTX1":"32080380326575683",
"KSKA1":"24254843881948059",
"NEOP1":"62884523179768200",
"NEOX1":"9807139177747641",
"HAMI1":"30167248101375870",
"HJPT1":"16369313804633525",
"HJPX1":"25129304172501430",
"TAYD1":"3722699128879020",
"TAYX1":"66234625721697786",
"HTOK1":"22260326095996531",
"HTOX1":"42892937789646488",
"HFRS1":"35424116338766901",
"HSHM1":"28809886765682162",
"HSHX1":"43667708360002073",
"KFJR1":"60968111020776674",
"KSHJ1":"60610861509165508",
"KSHX1":"14364842601603807",
"AZIN1":"42075223783409640",
"AZIX1":"22129017544200",
"ATIR1":"7483280423474368",
"ATIX1":"29716513021318095",
"KAVR1":"67059303301834130",
"KAVX1":"726401865204843",
"BHMN1":"26824673819862694",
"BHMX1":"12964716133621704",
"PKOD1":"42354736493447489",
"PKOX1":"25449662823397465",
"SZPO1":"4758266259250794",
"SZPX1":"6803271730717705",
"RTIR1":"22903901709044823",
"RTIX1":"41858326436945277",
"RADI1":"50185721305191887",
"RADX1":"2262715289665960",
"GHAT1":"70289374539527245",
"GHAX1":"56449205771773651",
"CHAR1":"33783140337377394",
"CHAX1":"14865390259501860",
"KRSN1":"43552974795606067",
"RIIR1":"12752224677923341",
"RIIX1":"12041217376571987",
"RINM1":"45895339414786358",
"RINX1":"26142199530487668",
"ZMYD1":"2589887561569709",
"ZMYX1":"38005238879860126",
"FNAR1":"32821908911812078",
"FNAX1":"24734871905109354",
"SIPA1":"44891482026867833",
"SIPX1":"590761101519570",
"KHSH1":"63915926161403347",
"KHSX1":"36675444072965904",
"SDRA1":"25165947991415904",
"SDRX1":"17184779097179305",
"KFAN1":"28033133021443774",
"KFAX1":"61581369333689993",
"KRIR1":"59217041815333317",
"KRIX1":"44678870441030319",
"SPDZ1":"51922189364308501",
"SPDX1":"46052543236360331",
"INDM1":"19257295292088310",
"INDX1":"1852132120586484",
"GOST1":"48990026850202503",
"GOSX1":"17237314339763699",
"LENT1":"14957056743925737",
"LENX1":"36110870923892956",
"NMOH1":"39436183727126211",
"NMOX1":"37350268082014292",
"TMKH1":"7457232989848872",
"TMKX1":"71186910349639777",
"MHKM1":"17330546482145553",
"MHKX1":"50722377181482963",
"MSTI1":"57273529732791251",
"MSTX1":"62221150547292335",
"MNSR1":"17834623106317041",
"MNSX1":"13010835010902276",
"IKCO1":"65883838195688438",
"IKCX1":"12088545433107773",
"MESI1":"31879190587976736",
"MESX1":"23552683239901730",
"DABO1":"61332057061846617",
"DABX1":"32679348534913643",
"DPAK1":"67988012428906654",
"DPAX1":"2501017203331667",
"DOSE1":"12387472624849835",
"DOSX1":"11936058301634784",
"DALZ1":"60451823714332895",
"DALX1":"3362850293262749",
"AMIN1":"50100062518826135",
"AMIX1":"41673962293011307",
"BDAN1":"48511238766369097",
"BDAX1":"46262771961973371",
"PDRO1":"70474983732269112",
"TMVD1":"34641719089573667",
"TMVX1":"18154205800023055",
"THDR1":"26114418513020265",
"THDX1":"11929836650963758",
"DJBR1":"33406621820337161",
"DJBX1":"18079534829579164",
"DAML1":"66450490505950110",
"DRZK1":"22255783119783047",
"DRZX1":"38007943162762758",
"ROZD1":"40262275031537922",
"ROZX1":"63452629875913229",
"DZAH1":"8915450910866216",
"DZAX1":"48879205486884942",
"DSOB1":"43622578471330344",
"DSOX1":"51063357877632134",
"DSBH1":"5866848234665627",
"DSBX1":"36667862403660976",
"DSIN1":"11432067920374603",
"DSIX1":"54299437423394846",
"DDPK1":"33603212156438463",
"DDPX1":"16630588761222078",
"ABDI1":"49054891736433700",
"ABDX1":"7585208964980608",
"DFRB1":"56550776668133562",
"DFRX1":"38285971158073841",
"FTIR1":"18303237082155264",
"FTIX1":"54711449369613330",
"DKSR1":"23353689102956991",
"DKSX1":"26314668128957507",
"KIMI1":"20024911381434086",
"KIMX1":"43588544194911344",
"EXIR1":"4384288570322406",
"EXIX1":"42538255636473499",
"DLGM1":"29247915161590165",
"DLGX1":"66766792660974984",
"IRDR1":"69090868458637360",
"PRDS1":"64988580376499833",
"INFO1":"40505767672724777",
"INFX1":"45097391187425276",
"EPRS1":"41048299027409941",
"EPRX1":"49613772749166261",
"TKIN1":"3823243780502959",
"TKIX1":"1723099959084685",
"RKSH1":"27952969918967492",
"RKSX1":"21500060221654011",
"MAPN1":"67126881188552864",
"MAPX1":"49532101082369992",
"ZPRS1":"33420285433308219",
"KOSR1":"42599305106713939",
"MAGS1":"5054819322815158",
"MAGX1":"44723997362573824",
"ABIK1":"70883594945615893",
"AZRT1":"28987829009893424",
"AZRX1":"35608558653140695",
"SDAB1":"4563413583000719",
"SDAX1":"68002468728896305",
"SADB1":"34890845654517313",
"SADX1":"62781722479769997",
"SURO1":"15949743338644220",
"SURX1":"14983273215576895",
"SAVE1":"25360782993370900",
"IRNT1":"36531083140502478",
"IRNX1":"69885094622785625",
"SBOJ1":"66295665969375744",
"SBOX1":"51223970438582603",
"SBHN1":"32525655729432562",
"SBHX1":"2122354233695079",
"SEPK1":"71856634742001725",
"SSEP1":"35669480110084448",
"SSEX1":"49361140703966185",
"SKPX1":"67223870501587101",
"PRMT1":"61436127547874135",
"SPID1":"45519261544951819",
"STEH1":"30829203706095076",
"STEX1":"37577414956190228",
"SKHS1":"4470657233334072",
"SKHX1":"15467183288337240",
"SKAZ1":"67327029014085707",
"SKAX1":"63310105340116493",
"KHOC1":"41974758296041288",
"KHOX1":"47827701898502941",
"SDST1":"27000326841257664",
"SDSX1":"16566273757667380",
"SDOR1":"27218386411183410",
"SDOX1":"48424973017498692",
"SROD1":"11964419322927535",
"SROX1":"11183410572675415",
"SSHR1":"26997316501080743",
"SSHX1":"4351174618872221",
"SIMS1":"6757220448540984",
"SIMX1":"23458117616920867",
"SEFH1":"10568944722570445",
"SEFX1":"41026060125059078",
"SSOF1":"13227300125161435",
"SSOX1":"2819110578357790",
"GDRS1":"69456730984618304",
"SGRB1":"52220424531578944",
"SGRX1":"65932581790240568",
"SFRS1":"41227201752535311",
"SFRX1":"53932269673520256",
"SFKZ1":"15521712617204216",
"SFKX1":"20593887444073437",
"FRDO1":"62422436072345198",
"FRDX1":"40750005236994995",
"SFAS1":"20603404633598318",
"SFAX1":"10716103455591194",
"SFNO1":"4528607775462304",
"SFNX1":"34774414473029882",
"SGEN1":"60654872678917533",
"SGEX1":"44969149970836673",
"SKRN1":"23742726069035026",
"SKRX1":"24544113280557261",
"SKOR1":"65321970913593427",
"SKOX1":"67682387713029178",
"SKER1":"15472396110662150",
"SKEX1":"3037464497437282",
"SMAZ1":"33808206014018431",
"SMAX1":"36927349282989093",
"SSNR1":"14231831499205396",
"SSNX1":"53536131398384570",
"SHZG1":"29747059672582491",
"SHZX1":"31159891095753824",
"SHGN1":"41284516796232939",
"SHGX1":"7486145189544149",
"SITA1":"10171945867136336",
"CIDC1":"37281199178613855",
"CIDX1":"34060949638085542",
"SYSM1":"47749661205825616",
"SEIL1":"14617104402836487",
"SEIX1":"48993230008229282",
"SMRG1":"28450080638096732",
"FSIN1":"2512214120008228",
"PARK1":"7711282667602555",
"PARX1":"63190039561056038",
"AMLH1":"16959429956899455",
"AMLX1":"14153483684603257",
"PNTB1":"48753732042176709",
"PNTX1":"7632696113249142",
"PNBA1":"35366681030756042",
"NBEH1":"22667016906590506",
"NBEX1":"20300372560291314",
"BMPS1":"61102694810476197",
"BMPX1":"9171279728707865",
"PAKS1":"11622051128546106",
"PAKX1":"68629328102697289",
"PABD1":"11640540339380126",
"PABX1":"68134183978822839",
"PRDZ1":"20562694899904339",
"PRDX1":"45231878301843366",
"PLAK1":"31920617569703557",
"PLAX1":"10549251453298737",
"PPAM1":"38417665293111458",
"PPAX1":"36597927530072864",
"PNES1":"7745894403636165",
"PNEX1":"70885929611298658",
"PTEH1":"51617145873056483",
"THSH1":"49831372632909204",
"THSX1":"63950064557947536",
"TOPI1":"67422066034966650",
"TOPX1":"32768389062627654",
"NJEY1":"30007580613586002",
"PKHA1":"70934270174405743",
"PKHX1":"67424359693542598",
"DODE1":"40611478183231802",
"DODX1":"32775115857585121",
"SHRG1":"55761337960556026",
"SHRX1":"31312374884749268",
"ZNGN1":"9049928781611298",
"ZNGX1":"27441338542049382",
"SEPP1":"49188729526980541",
"TAMN1":"2400322364771558",
"TSAL1":"26785345607979150",
"TSAX1":"56145524393016216",
"SHSI1":"30974710508383145",
"SHSX1":"1860384396424573",
"PESF1":"14733297998516697",
"PESX1":"37397450502348400",
"PGDR1":"21772258644715569",
"SHFA1":"36899214178084525",
"PFRB1":"67965884006655065",
"PFRX1":"6393093854932837",
"SHFS1":"43781018754867729",
"SHFX1":"33124462307941707",
"PFAN1":"65122215875355555",
"PFAX1":"55622199783443721",
"CRBN1":"27308217070238237",
"CRBX1":"10157407031358922",
"KAFF1":"180774784936665",
"KAFX1":"68215194515227175",
"NKOL1":"62177651435283872",
"NKOX1":"33505686728824629",
"GTSH1":"44153164692325703",
"GTSX1":"46167643644457680",
"LEAB1":"39116664428676213",
"LEAX1":"66183408418816482",
"SLVN1":"14900251521017020",
"MAVA1":"29915504190030439",
"MAVX1":"13279993223440273",
"NPRS1":"14073782708315535",
"NPRX1":"23142133203996048",
"VASH1":"46778692022402356",
"VASX1":"36875068201975202",
"SHOY1":"3493306453706327",
"PSHZ1":"38568786927478796",
"PSHX1":"19717343975708874",
"SSIN1":"35796086458096255",
"SSIX1":"8992202615765020",
"PIAZ1":"35158826900216508",
"PIAX1":"22096199430853991",
"KLBR1":"24303422207378456",
"KLBX1":"55490250330757201",
"SBEH1":"42387718866026650",
"SBEX1":"17080537778426884",
"BEPP1":"29650505265356603",
"BEPX1":"10125150304958552",
"BENN1":"17059960254855208",
"BENX1":"38770731314949641",
"LPAK1":"34032872653290886",
"LPAX1":"6544645716121372",
"MINO1":"18401147983387689",
"MINX1":"13308396407628501",
"CHCH1":"44850033148208596",
"CHCX1":"13083555452743181",
"KDPS1":"2254054929817435",
"KDPX1":"52139501202126140",
"DMOR1":"2434703913394836",
"DMOX1":"59887874326934221",
"ZARM1":"4369934250728330",
"SASN1":"51229318675210816",
"SASX1":"40309575177709730",
"SLMN1":"28672095850798501",
"SLMX1":"48926251886441092",
"SHPZ1":"59921975187856916",
"SHPX1":"2705253775088582",
"SPKH1":"31791737198597563",
"SPKX1":"15581863918201593",
"SPPE1":"61506294208022391",
"SPPX1":"20272770791380597",
"SHAD1":"20487994977117557",
"SHAX1":"36771749618541632",
"KRSH1":"62404730109947970",
"GORJ1":"31024260997481994",
"GORX1":"53482856220074779",
"GCOZ1":"22299894048845903",
"GCOX1":"30551124291517887",
"MRGN1":"52975109254504632",
"MRGX1":"50773402681099358",
"MRAM1":"6131290133202745",
"MRAX1":"63552922113415543",
"RNAB1":"29631596152440287",
"RNAX1":"27576096486410105",
"NOSH1":"48619517949257749",
"NOSX1":"10134751929001651",
"KIVN1":"21940781391333638",
"KIVX1":"69848800705652106",
"AZAB1":"38547060135156069",
"AZAX1":"68708769838923502",
"MARK1":"20865316761157979",
"PKLJ1":"25244329144808274",
"KSIM1":"66701874099226162",
"KSIX1":"65614373112361128",
"ALTK1":"70849059438036431",
"ALTX1":"55163494925650570",
"SAMA1":"34673681828119297",
"SAMX1":"3727693296236633",
"NLAH1":"71492985674836424",
"NLAX1":"40526606175393916",
"ALIR1":"65004959184388996",
"ALIX1":"36600889395640293",
"BAHN1":"66772024744156373",
"BMAS1":"16663779781503749",
"BMAX1":"62972959180501542",
"BIRI1":"31892548539456357",
"BIRX1":"26601876609464268",
"ALPS1":"8559354261956680",
"ALPX1":"45801323230963889",
"SPTA1":"68488673556087148",
"SPTX1":"24832054403183361",
"JAMD1":"30765727085936322",
"JAMX1":"42201186298844859",
"FAJR1":"41302553376174581",
"FAJX1":"5898511005624629",
"JSHO1":"22742134293057021",
"JSHX1":"46661780956927518",
"FKAS1":"4733285133017464",
"FKAX1":"5550649038347558",
"FKHZ1":"28864540805361867",
"FKHX1":"13628968289488697",
"FRVR1":"408934423224097",
"FRVX1":"41317265011382362",
"FRIS1":"54419429862704331",
"FRIX1":"10079795343879888",
"TFKR1":"56585229755651616",
"TFKX1":"22314977867866119",
"LSAH1":"62620182261149083",
"FSAZ1":"12874072841236826",
"FSBZ1":"37284308569715577",
"SEPA1":"8977441217024425",
"SEPX1":"15731047379849033",
"LSDD1":"36608426654628266",
"LSDX1":"69259498999037661",
"SORB1":"54277068923045214",
"SORX1":"3505675353152597",
"SOLI1":"58892839837671228",
"SOLX1":"71756156794073862",
"LAMI1":"25286509736208688",
"LAMX1":"33658726815807637",
"LMIR1":"48623320733330408",
"LMIX1":"58242024190036642",
"PMET1":"44571627722410412",
"PMEX1":"1518157759350339",
"ALMR1":"18004480270695404",
"ALMX1":"2050740941534952",
"MSMI1":"35425587644337450",
"MSMX1":"8731565448647588",
"ENAZ1":"56240779529754100",
"ENAX1":"50545475113911465",
"NALM1":"57875847776839336",
"NALX1":"34404581741939737",
"NGFO1":"56324206651661881",
"NGFX1":"8175268772799530",
"FVAN1":"20253580805051293",
"FVAX1":"48473870645523269",
"FOLD1":"46348559193224090",
"FOLX1":"37018498887928862",
"FAIR1":"40808043719554948",
"FAIX1":"53249498382937694",
"GPRS1":"47477233032133723",
"GPRX1":"41727358876253319",
"GPSH1":"67030488744129337",
"GPSX1":"42230292145842208",
"GSBE1":"44967158778304588",
"GSBX1":"49384226669172647",
"GTOR1":"60021765857012878",
"GTOX1":"37451083085805929",
"GARN1":"39610074039667804",
"GARX1":"32669817266382439",
"GGAZ1":"15259343650667588",
"GGAX1":"55042339780346549",
"GGOH1":"24683827262592815",
"GGOX1":"71944697706421313",
"GBIS1":"33634705189692362",
"GBIX1":"54071352171589816",
"GSHI1":"30535783752961355",
"GSHX1":"28678187324376436",
"SHKR1":"35964395659427029",
"SHKX1":"20381036241470518",
"GHND1":"37631109616997982",
"GHNX1":"42965645001665951",
"GBJN1":"18356933039391862",
"GBJX1":"47752890804996793",
"GESF1":"40411537531154482",
"GESX1":"17197203950543191",
"GLOR1":"56820995669577571",
"GLOX1":"47415456025309183",
"GMRO1":"43342306308122676",
"GMRX1":"57007700552650971",
"GNJN1":"34454945407422432",
"GNJX1":"64635313423278212",
"GNBO1":"63380098535169030",
"GNBX1":"55205982891279789",
"GHEG1":"14398278072324784",
"GHEX1":"49762562284200125",
"ABGN1":"56040335629505100",
"ABGX1":"47134988689244518",
"NSAZ1":"49353447565507376",
"NSAX1":"25896842749407120",
"KESF1":"55747512772958281",
"KESX1":"57576691407491832",
"KALA1":"44549439964296944",
"BAMA1":"4942127026063388",
"BAMX1":"58330599921175874",
"KVEH1":"60350996279289099",
"KVEX1":"59525964192678026",
"ITAL1":"13196430375349226",
"ITAX1":"24117226355581020",
"IRGC1":"37369138117139150",
"IRGX1":"51800153073527165",
"BAFG1":"43256212620530446",
"BAFX1":"40029719755707991",
"KBRS1":"37366608481858080",
"KPRS1":"9698674686691945",
"KPRX1":"58024357149774390",
"PSIR1":"57639364758870873",
"PSIX1":"5920319552619760",
"TKSM1":"24085906177899789",
"TKSX1":"36019565007303075",
"CHML1":"18027801615184692",
"CHMX1":"43356599956782034",
"CHIR1":"55376450081365373",
"CHIX1":"44034797904823034",
"KHFZ1":"32257753560585502",
"KHFX1":"29075808594290931",
"KCHI1":"16405556680571453",
"KCHX1":"56572417882819500",
"DMVN1":"3623921205367364",
"DMVX1":"28711499450482077",
"TSRZ1":"57086055330734195",
"TSRX1":"41733197666474598",
"PKER1":"38437201078089290",
"PKEX1":"66733343177003497",
"ROOI1":"22787503301679573",
"ROOX1":"29184718087541648",
"SISH1":"28325731560106431",
"SISX1":"25879082553156895",
"SINA1":"25001509088465005",
"SINX1":"13482565247432073",
"ARDK1":"4614779520007780",
"ARDX1":"20044076668988655",
"PSER1":"20560887114747719",
"PSEX1":"9866485009925582",
"KSAD1":"29122854902865456",
"KSAX1":"1314853494617240",
"TBAS1":"8977369674477111",
"TBAX1":"10168197471714005",
"NSPS1":"19471788163911687",
"NSPX1":"65836038919989820",
"NASI1":"23837844039713715",
"NASX1":"20622681776256207",
"SHQZ1":"13279867471688540",
"SHQX1":"140099686459313",
"SGAZ1":"62346804681275278",
"GOLG1":"35700344742885862",
"ALVN1":"32678431934327184",
"ALVX1":"45727447257267582",
"TAMI1":"67690708346979840",
"TAMX1":"65916883530316213",
"MNGZ1":"50341528161302545",
"MNGX1":"66630516232885208",
"KNRZ1":"20411759370751096",
"KNRX1":"43501047082635150",
"NILO1":"786234965064488",
"NILX1":"42586304445866872",
"BHSM1":"11278802993290837",
"BHSX1":"55500657710269413",
"SHMD1":"67206358287598044",
"SHMX1":"35955196754615835",
"VARZ1":"58097053240000607",
"VARX1":"56738062726001817",
"KVIR1":"43545527030854340",
"KVIX1":"19174812964848627",
"KYAN1":"45353845483523901",
"ASAL1":"63363116407864462",
"ASAX1":"43124071611770324",
"AZMA1":"59915902185156694",
"AZMX1":"21405564783526739",
"TBHM1":"23295417816476597",
"TBHX1":"25524501289667446",
"BOTA1":"30650426998863332",
"BOTX1":"70528526190252660",
"PELC1":"5187018329202415",
"PELX1":"3388451018224720",
"IRPO1":"17393119378053108",
"IRPX1":"13312547588339850",
"PYAM1":"38297715702941775",
"PYAX1":"10625146599769364",
"JJNM1":"67093405131120717",
"JJNX1":"67621826314697621",
"LKPS1":"43685510232615301",
"LKPX1":"6912445055737597",
"KHAZ1":"65414507129586385",
"KHAX1":"69377916525018465",
"SRMA1":"55897939403232751",
"SRMX1":"244106582239634",
"KMOA1":"21758758306221606",
"KMOX1":"46035314754119963",
"SMRI1":"36774567041364173",
"SMRX1":"57462267975967417",
"LTOS1":"59142194115401696",
"LTOX1":"43455612336353491",
"BVMA1":"29860265627578401",
"BVMX1":"13461179188856487",
"MOBN1":"27922860956133067",
"MDAR1":"19990581743778955",
"DADE1":"65999092673039059",
"DADX1":"12639781184165880",
"IAGM1":"23838634016123354",
"IAGX1":"66546619320950880",
"BMEL1":"13611044044646901",
"BMEX1":"5811747532754081",
"MDKO1":"33441514568901717",
"MDKX1":"18733719742989734",
"BROJ1":"60061422939859083",
"BROX1":"55943815270366220",
"NBRS1":"60095061789823130",
"PTOS1":"71499289762741257",
"PTOX1":"29112217893232632",
"NKLA1":"10919655792568926",
"MRIN1":"30231789123900526",
"MRIX1":"2855515398698068",
"NORI1":"19040514831923530",
"HWEB1":"43362635835198978",
"HMRZ1":"68635710163497089",
"HMRX1":"25328018826422512",
"TAZB1":"1358190916156744",
"TAZX1":"48981174642799639",
"KARA1":"29244787813932382",
"KARX1":"38203540900047502",
"ATDM1":"33541897671561960",
"ATDX1":"61399677811943715",
"IDOC1":"47841327496247362",
"IDOX1":"7619581461589857",
"ALBZ1":"57944184894703821",
"OIMC1":"52232388263291380",
"OIMX1":"36293785932444419",
"BANS1":"49776615757150035",
"BNAX1":"56271726572478068",
"LIRZ1":"3149396562827132",
"BANK1":"48010225447410247",
"BANX1":"8279693426955446",
"TSBE1":"13937270451301973",
"TSBX1":"62275280734625819",
"BSDR1":"28320293733348826",
"BMLT1":"778253364357513",
"BMLX1":"25043059770705816",
"SBAH1":"18063426072758458",
"SBAX1":"58198007384583512",
"BALI1":"28328710198554144",
"BALX1":"23185568638908069",
"BIME1":"11773403764702778",
"BIMX1":"59735609117437896",
"BPAR1":"33293588228706998",
"BPAX1":"19853987870179776",
"BPAS1":"9536587154100457",
"BPSX1":"53374821490063799",
"PETR1":"59486059679335017",
"PETX1":"31435545119454895",
"DARO1":"7183333492448248",
"DARX1":"67979306676078989",
"BPST1":"22087269603540841",
"BTEJ1":"63917421733088077",
"BTEX1":"57027493672958737",
"TGOS1":"68117765376081366",
"TGOX1":"46270513972980340",
"TMEL1":"17528249960294496",
"TMEX1":"2362491091971813",
"TSHE1":"54676885047867737",
"TSHX1":"63689155520282158",
"TOSA1":"2944500421562364",
"TOSX1":"20278348345530119",
"TOKA1":"47232550823972469",
"TOKX1":"25387056990464790",
"IKHR1":"7395271748414592",
"IKHX1":"27729386420118206",
"BKHZ1":"47333458678352378",
"BKHX1":"25661711955019337",
"RENA1":"7385624172574740",
"RENX1":"55274159604040834",
"SSAP1":"37614886280396031",
"SSAX1":"26643740599997035",
"SAKH1":"25514780181345713",
"SAKX1":"3679885359158219",
"OS031":"7768327419174840",
"OS011":"65774725600261203",
"OS021":"35282121039020302",
"OS061":"44411078630612905",
"SPAH1":"2328862017676109",
"SPAX1":"54287510798838485",
"OS091":"10191122735393627",
"OS111":"47362853625306007",
"OS121":"5454781314262062",
"SDID1":"61276682443262105",
"SDIX1":"17153727206566342",
"OS101":"51185499879934793",
"OS131":"36857080203588624",
"OS041":"11827297444577200",
"OS161":"71335098849021006",
"OS171":"41011426560490365",
"OS181":"55850912428859273",
"SKBV1":"11258722998911897",
"SKBX1":"5818838554339991",
"OS191":"37351190176977060",
"OS211":"59462881877083131",
"OS201":"64217006537761390",
"OS221":"68870496728320072",
"OS231":"1277592884769853",
"OS241":"55916539620839777",
"OS251":"58358543014279572",
"OS261":"11358107932902023",
"OS081":"16843404477481740",
"OS271":"19511179561056679",
"OS281":"46820237871803554",
"OS291":"22318795784160675",
"OS301":"63570910379296908",
"OS151":"16370154440238855",
"OS051":"59652306881376415",
"VSIN1":"45050389997905274",
"VSIX1":"10814280156273322",
"GBEH1":"46982154647719707",
"GBEX1":"15406006540387078",
"SAND1":"37204371816016200",
"SANX1":"39419948282087552",
"SNMA1":"57309221039930244",
"SNMX1":"43740308126125261",
"GDIR1":"26014913469567886",
"GDIX1":"30756584974640550",
"KRAF1":"47996917271187218",
"KRAX1":"56772105873719945",
"LPRS1":"48241092863917835",
"RSAP1":"45174198424472334",
"RSAX1":"59957747873181306",
"LSMD1":"71744682148776880",
"LSMX1":"19216138630342675",
"LKGH1":"23086515493897579",
"LKGX1":"59430351461797798",
"LKAR1":"61469668095573716",
"VLMT1":"11403770140000603",
"VLMX1":"4039883656662701",
"VALE1":"5968811612822747",
"LZIN1":"20946530370469828",
"LZIX1":"34731841379388186",
"VMDR1":"30447901674051381",
"MADN1":"58931793851445922",
"MADX1":"66240430785255272",
"MOIN1":"57498323844693360",
"MELT1":"6626302649460766",
"MELX1":"62074720294882247",
"GMEL1":"41796741644273824",
"GMEX1":"3852548583453231",
"NAFT1":"33931218652865616",
"NAFX1":"3893110467363738",
"NOVN1":"47302318535715632",
"NOVX1":"70657803623349012",
"SNRO1":"62603302940123327",
"SNRX1":"59061939785593482",
"NIKI1":"25336820825905643",
"NIKX1":"26090464295830176"
}

def stockdetail(stock,type="namad"):
    index_url_list="http://www.tsetmc.com/Loader.aspx?ParTree=111C1417"
    fopen=rq.get(index_url_list).content
    df_stock_list=pd.DataFrame(pd.read_html(io.StringIO(fopen.decode("utf-8")),
                                 header=0,index_col=4)[0])

    try:
        if stock=="list":
            return df_stock_list["نام"]
        else:
            if type=="enamad":
                return(df_stock_list.loc[stock]["نام"])
            elif type=="full":
                return(df_stock_list.loc[stock])
            elif type=="name":
                return(df_stock_list[df_stock_list["نام"]==stock].index.values[0])
            elif type=="namadf":
                return(df_stock_list[df_stock_list["نماد.1"]==stock].index.values[0])
            elif type=="namad":
                return(df_stock_list[df_stock_list["نماد.1"]==stock].T)
    except:
        print("Error! stock not found.")
    
def stocklist():
    return stocknames.keys()
def stock(stockname="",value=100,newfile=False,standard=False,namadf=True):
    if namadf==True:
        stockname=stockdetail(stockname,type="namadf")
    try:
        urlid = stocknames[stockname.upper()]
        url = 'http://www.tsetmc.com/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i=' + urlid
        #Read file content
        try:
            if newfile==False:
                df = pd.read_csv(stockname+'.csv',index_col="<DTYYYYMMDD>",parse_dates=True)
            else:
                raise FileNotFoundError        
        except FileNotFoundError:
            print("Download New file ....")
            fopen=rq.get(url).content
            df=pd.read_csv(io.StringIO(fopen.decode("utf-8")),index_col="<DTYYYYMMDD>",parse_dates=True)
            df.to_csv(stockname+".csv")   
        if standard==False:
            return (df.head(value))
        elif standard==True:
            df=df.rename(columns={"<OPEN>": "Open", "<CLOSE>": "Close","<HIGH>":"High",
                                  "<LOW>":"Low","<VOL>":"Volume"})
            df.index.rename('Date',inplace=True)
            df.drop(["<TICKER>","<FIRST>","<VALUE>","<OPENINT>","<PER>","<LAST>"], axis=1, inplace=True)
            return (df.head(value))


    except:
        print("stockname Not Found, Please try again ...")

