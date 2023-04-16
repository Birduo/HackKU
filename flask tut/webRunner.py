from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route("/state")
def local_area():
    return render_template('first.html')


@app.route('/plants', methods=["GET", "POST"])
def plants():
    '''
    if request.method == "POST":
        plants = request.form.get("State")

        return "The best plants for you are: "+plants
    '''
    _results = [{'common_name': 'Blue funnel-lily', 'description': 'Leaves 10-30(-35) * 0.15-0.3 cm. Scape 1-2(-3.5) dm, entirely glabrous. Inflorescences 2-6(-9)-flowered. Flowers: perianth light blue to violet-purple, 1.5-2.5(-3) cm, lobes shorter than to ca. as long as tube; anthers 2-4 mm; pedicel 1-2(-2.5) cm. Capsules 1-1.5 cm. Seeds 7-9 mm.', 'image_url': 'None', 'name': 'Androstephium coeruleum', 'states': "['Kansas', 'Oklahoma', 'Texas']"}, {'common_name': 'N/A', 'description': 'Herbs, erect or ascending, rarely rooting at nodes. Stems absent or 2-7 cm in flower, to 20 cm in fruit, shaggy pilose to villous. Leaves: blade green, linear-lanceolate, 4-30 * 0.9-2.5 cm (distal leaf blades equal to or narrower 
than sheaths when sheaths opened, flattened), margins frequently clear or edged with rose, laxly and irregularly pilose or villous. Inflorescences terminal, solitary; bracts foliaceous, well developed, not saccate, sparsely to densely pilose. Flowers distinctly pedicillate; pedicels 4-6 cm, laxly pilose; sepals usually purple or rose-colored (rarely pale green), not inflated, 1.2-1.6 cm, uniformly eglandular-pilose; petals distinct, deep rose or purple, or frequently blue, broadly ovate, not clawed, 1.8-2.2 cm; stamens free; 
filaments bearded. Capsules 5-7 mm. Seeds 2-3 mm. 2n = 24.', 'image_url': 'None', 'name': 'Tradescantia tharpii', 'states': "['Kansas', 'Missouri', 'Oklahoma']"}, {'common_name': 'N/A', 'description': 'Stems usually erect, green with red or purple at base and apex of segments and around flowers, often becoming completely red in fruit, simple or with primary and secondary branches, more elaborately branched if damaged, (1-)5-25 cm, ultimate branches usually short; leaf and bract apices obtuse to subacute, not mucronate. Spikes weakly torulose, 0.5-3(-5) cm, with 4-10(-19) fertile segments; bracts covering only base of cymes. Fertile segments (2d-4th in main spikes) 2.1-4.4 * 1.8-3.2 mm, about as long as wide or slightly longer, widest distally, margins (0.1-)0.2-0.3(-0.4) mm wide, scarious. Central flowers usually semicircular distally, 1.1-2.2 * 1-1.7 mm, about as long as 
wide or a little longer, usually not or scarcely larger than lateral flowers; anthers commonly not exserted, (0.2-)0.3-0.4 mm, usually dehiscing within flowers. 2n = 18.', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Salicornia_rubra_%E2%80%94_Matt_Lavin_010.jpg/220px-Salicornia_rubra_%E2%80%94_Matt_Lavin_010.jpg', 'name': 'Salicornia rubra', 'states': "['Iowa', 'Kansas', 'Minnesota', 'Nebraska', 'Nevada', 'North Dakota', 'South Dakota', 'Utah']"}, {'common_name': 'Brown-spined pricklypear', 'description': 'Shrubs, decumbent to commonly trailing, 0.3-1 m. Stem segments not disarticulating, green to dark green, sometimes reddish under stress, flattened, obovate to circular, 10-25 * 7-20 cm, low tuberculate, glabrous; areoles 5-7 per diagonal row across midstem segment, obovate to elliptic, 3-6 * 2-4 mm; wool tan to brown, aging grayish. Spines (0-)2-8 per areole, at most areoles to only distal 1/4 of stem segment, or essentially absent, brown to white, straight, curved, or spirally twisted; major central spines deflexed 
or spreading, brown to red-brown (to blackish), or partly to wholly gray to tan, subulate, usually flattened near base, 30-80 mm; abaxial spines usually 1-3, deflexed, white, flattened, shorter, to 20 mm. Glochids dense in crescent at adaxial edge of areole and subapical tuft, tan to red-brown, to 5 mm. Flowers: inner tepals yellow with red basal portions (rarely entirely pink to red), 30-40 mm; filaments greenish basally, pale yellow to white distally; anthers yellow; style white; stigma lobes green to yellow-green. Fruits wine red to purple, with greenish flesh (sometimes reddish and ± juicy), not long stipitate, obovate to barrel-shaped, 30-50 * 20-30 mm, fleshy, glabrous, spineless; areoles 18-24. Seeds tan, subcircular, 4-5 mm diam., evidently notched, warped; girdle protruding 1 mm. 2n = 66.', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Opuntia_phaeacantha_kz2.jpg/220px-Opuntia_phaeacantha_kz2.jpg', 'name': 'Opuntia phaeacantha', 'states': "['California', 'Kansas', 'Oklahoma', 'Texas']"}, {'common_name': 'N/A', 'description': 'Plants forming diffuse or dense clones. Roots arising at nodes. Petioles 2-20 cm, sparsely pubescent. Pinnae 4-19 * 4-16 mm, pubescent to glabrous. Sporocarp stalks erect, unbranched, attached at base of petiole (occasionally up to 3 mm above it), not hooked at apex, 0.5-25 mm. Sporocarps perpendicular or slightly nodding, 3.6-7.6 * 3-6.5 mm, 1.5-2 mm thick, elliptic to nearly round in lateral view, pubescent but soon glabrate, scars left by fallen trichomes often appearing as purple or brown specks; raphe 1.1-1.7 mm, proximal tooth 0.3-0.6 mm, blunt, distal tooth 0.4-1.2 mm, acute, often hooked at apex. Sori 14-22.', 'image_url': 'None', 'name': 'Marsilea vestita', 'states': "['Alabama', 'Arkansas', 'Florida', 'Iowa', 'Kansas', 'Louisiana', 'Minnesota', 'Mississippi', 'Nebraska', 'North Dakota', 'Oklahoma', 'South Dakota']"}, {'common_name': 'White beardtongue', 'description': 'Stems ascending to erect, (10-)15-50(-55) cm, retrorsely hairy proximally, glandular-pubescent distally. Leaves basal and cauline, not leathery, glabrate or puberulent to scabrous; basal and proximal cauline petiolate, 20-85(-110) * (4-)7-18(-20) mm, blade oblanceolate or obovate to lanceolate, base tapered, margins entire to obscurely or distinctly serrate, apex obtuse to acute; cauline 2-5(or 6) pairs, sessile or proximals short-petiolate, 25-65 * (3-)7-19(-21) mm, blade ovate to lanceolate, base tapered to clasping, margins entire or serrate to dentate, apex acute. Thyrses continuous or interrupted, cylindric, 4-24(-30) cm, axis densely glandular-pubescent, verticillasters (2 or)3-10, cymes 2-7-flowered, 2 per node; proximal bracts lanceolate, 17-65 * 3-17 mm; peduncles and pedicels densely glandular-pubescent. Flowers: calyx lobes ovate to lanceolate, 4-7 * 1.5-3 mm, glandular-pubescent; corolla white, rarely tinged pink or lavender, with red or reddish purple nectar guides, funnelform, (12-)16-20 mm, glandular-pubescent internally, tube 4-6 mm, throat gradually inflated, not constricted at orifice, (4-)6-8 mm diam., rounded abaxially; stamens included, pollen sacs opposite, explanate, 0.7-1.1 
mm, dehiscing completely, sutures smooth; staminode 8-9 mm, included, 0.3-0.4 mm diam., tip straight to recurved, distal 3-6 mm sparsely to moderately villous, hairs yellowish, 
to 1 mm; style 9-11(-13) mm. Capsules 8-12 * 4-7 mm. 2n = 16.', 'image_url': 'None', 'name': 'Penstemon albidus', 'states': "['Colorado', 'Iowa', 'Kansas', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Oklahoma', 'South Dakota', 'Wyoming']"}, {'common_name': 'Hoary goldenaster', 'description': 'Perennials, 15-40(-65) cm; taprooted, frequently rhizomatous (clonal). Stems 1-75, ascending to erect (proximaly sometimes reddish brown, often whitish due to pubescence, sometimes brittle), often short-branched in distal 1/2, usually sparsely long-hispid (more so in tetraploids), distally strigoso-canescent, eglandular (axillary leaf fascicles often present). Leaves generally ascending, congested; proximal cauline petiolate or subsessile, blades oblanceolate, 19-32 * 2-6 mm, bases convex-cuneate to attenuate, margins flat, entire, strigoso-ciliate, proximally long-hispido-strigose, apices acute, faces densely strigose, long-hispid hairs few, eglandular; distal sessile, usually silvery gray-green, blades linear-oblanceolate, 11-29 * 2-5 mm, little reduced distally, apices acute, faces very to extremely densely strigoso-canescent (90-200 hairs/mm²; silvery-whitish), long-hispid hairs usually few, eglandular. Heads 1-9(-15), borne singly or in corymbiform arrays, branches ascending. Peduncles 2-10 mm, densely strigose, usually sparsely hispid; bracts grading from leaves, proximal oblanceolate, sometimes little reduced distally; long, linear-oblancelate, leaflike bracts often subtending heads. Involucres cylindric to narrowly campanulate, 5-7(-7.5) mm (shorter than disc florets). Phyllaries in 4-6 series, linear-lanceolate to lanceolate, unequal (outer lengths 1/5-1/4 inner), margins scarious, distally ciliate and reddish purple, faces moderately strigose, eglandular. Ray florets 10-22; laminae 5-9(-10.5) * 0.8-1.4 mm. Disc florets (14-)22-40(-50); corollas ± ampliate, 4.7-6.5 mm, throats glabrous, lobes 0.5-0.75 mm, lobes sparsely pilose (hairs 0.1-0.25 mm). Cypselae monomorphic, obconic, compressed, 1.2-3.1 mm, ribs 6-10 (sometimes brownish), faces moderately strigose; pappi off-white, outer of linear scales 0.25-0.5 mm, inner of 25-40 bristles 5-7.5 mm, longest weakly clavate. 2n = 18, 36.', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Heterotheca_canescens.jpg/220px-Heterotheca_canescens.jpg', 'name': 'Heterotheca canescens', 'states': "['Kansas', 'Missouri', 'Oklahoma', 'Texas']"}, {'common_name': 'Texas bull-nettle', 'description': 'Plants (30-)40-50(-100) cm. Leaves: stipules 3-4 mm, margins usually deeply toothed, rarely entire; petiole 5-18 cm; blade ± round in outline, 6-15 cm 
diam., deeply lobed, lobes 3/5-4/5 blade length, base broadly cordate, margins dentate, teeth and lobe apices acute, not aristate. Staminate flowers: calyx funnel-shaped, tube 12-17 mm, distally flaring, stinging hairs present, lobes 10-17 mm; stamens of outer whorl shorter than inner, filaments of outer whorl distinct or connate basally, of inner whorl connate most of length; staminodes 0. Pistillate flowers: sepals 15-25 mm; stigmas 12-24. Capsules 15-20 mm. Seeds brown, sometimes mottled, 14-18 mm. 2n = 36.', 'image_url': 
'None', 'name': 'Cnidoscolus texanus', 'states': "['Arkansas', 'Kansas', 'Louisiana', 'Oklahoma', 'Texas']"}, {'common_name': 'Actée rouge', 'description': 'Leaf blade: leaflets abaxially glabrous or pubescent. Inflorescences at anthesis often as long as wide, pyramidal. Flowers: petals acute to obtuse at apex; stigma nearly sessile, 0.7-1.2 mm diam. during anthesis, much narrower than ovary. Berries red or white, widely ellipsoid, 5-11 mm; pedicel dull green or brown, slender, 0.3-0.7 mm diam., thinner than axis of raceme. Seeds 2.9-3.6 mm. 2n = 16.', 'image_url': 'None', 'name': 'Actaea rubra', 'states': "['Alaska', 'Illinois', 'Iowa', 'Kansas', 'Minnesota', 'Nebraska', 'New Mexico', 'North Dakota', 'South Dakota', 'Wisconsin']"}, {'common_name': 'Arkansas yucca', 'description': 'Plants forming small colonies, acaulescent or caulescent; rosettes usually small. Stems decumbent, short, to 0.2 m. Leaf blade mostly yellowish green, flattened, grasslike, concavo-convex, widest near middle, 20-60(-70) * 0.7-2(-2.5) cm, flexible, margins entire, curled, filiferous, apex long, tapering to short spines 1.6-3.2 mm. Inflorescences racemose, occasionally paniculate proximally, arising within rosettes or at rosette level, 3-6(-8) 
dm, glabrous; bracts erect; peduncle scapelike, 0.2-0.5(-0.6) m, 0.3-0.7(-1.3) cm diam. Flowers pendent; perianth globose; tepals distinct, greenish white, elliptic to orbicular or oblong, 3.2-6.5 * 2-5 cm; filaments 1.3-2.5 cm; anthers 3.2 mm; pistil 2.5-2.8(-3.2) cm; style dark green, 7-13 mm, tumid; stigmas lobed. Fruits erect, capsular, dehiscent, 
oblong-cylindric to obovoid, constricted near middle, stout, 4-6.5(-7) * 2-3 cm, dehiscence septicidal. Seeds dull black, thin, ca. 1 cm diam.', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Yucca_arkansana_fh_1185.30_TX_B.jpg/220px-Yucca_arkansana_fh_1185.30_TX_B.jpg', 'name': 'Yucca arkansana', 'states': "['Arkansas', 'Kansas', 'Louisiana', 'Missouri', 'Oklahoma', 'Texas']"}]
    return render_template("plant.html", results = _results)