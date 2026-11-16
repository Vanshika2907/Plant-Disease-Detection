"""Final 68-class educational plant-disease knowledge base.

Source support is partial for some labels; see each entry review_status.
No pesticide products or dosages are prescribed.
"""

KNOWLEDGE_BASE = {'Apple___Apple_scab': {'causal_agent': 'Venturia inaequalis',
                        'chemical_treatment': None,
                        'condition': 'Apple scab',
                        'crop': 'Apple',
                        'diagnostic_caution': 'The model predicts a dataset label from an image; '
                                              'it does not confirm the pathogen, distinguish all '
                                              'look-alike conditions, or assess disease severity.',
                        'management': ['Remove or thoroughly shred fallen infected leaves after '
                                       'leaf fall to reduce the overwintering source of spores.',
                                       'Prune appropriately to improve canopy air movement and '
                                       'shorten leaf-wetness periods.',
                                       'Monitor susceptible new foliage during wet spring periods '
                                       'because infection risk is greatest when young tissue '
                                       'remains wet.'],
                        'nutrient_guidance': None,
                        'prevention': ['Sanitize the orchard floor by removing or accelerating '
                                       'decomposition of scab-infected leaf litter.',
                                       'Maintain an open canopy so leaves dry more quickly after '
                                       'rain or irrigation.',
                                       'Use disease-resistant or less-susceptible cultivars where '
                                       'suitable for the growing region.'],
                        'review_status': 'REQUIRES_SOURCE_REVIEW',
                        'sources': [{'organization': 'University of Minnesota Extension',
                                     'title': 'Apple Scab',
                                     'url': 'https://apps.extension.umn.edu/garden/diagnose/plant/fruit/apple/leavesspots.html'}],
                        'spread': ['The fungus survives in fallen infected apple leaves and '
                                   'produces spores during wet spring conditions.',
                                   'Spores are carried by rain splash onto newly developing leaves '
                                   'and fruit.',
                                   'Extended periods of leaf wetness favor infection and secondary '
                                   'spread.'],
                        'symptoms': ['Olive-green to brown leaf spots with irregular or feathered '
                                     'margins that darken with age.',
                                     'Leaves may yellow and drop prematurely when infection is '
                                     'severe.',
                                     'Brown, raised, corky lesions develop on fruit; severely '
                                     'affected fruit can become distorted or cracked.'],
                        'treatment_note': 'Disease management should be based on local '
                                          'disease-risk conditions and crop-stage guidance. No '
                                          'chemical treatment is prescribed by this educational '
                                          'knowledge base.',
                        'type': 'Fungal Disease'},
 'Apple___Black_rot': {'causal_agent': 'Botryosphaeria obtusa',
                       'chemical_treatment': None,
                       'condition': 'Apple black rot',
                       'crop': 'Apple',
                       'diagnostic_caution': 'The model predicts a dataset label from an image; it '
                                             'does not confirm the pathogen, distinguish all '
                                             'look-alike conditions, or assess disease severity. '
                                             'Confirm uncertain cases with a qualified '
                                             'plant-health professional.',
                       'management': ['Prune out dead or diseased wood and remove mummified fruit '
                                      'rather than leaving them in the canopy.',
                                      'Pay particular attention to dead branches, pruning stubs '
                                      'and other woody material that can harbor the fungus.',
                                      'Avoid creating unnecessary wounds and address tree stress '
                                      'that leaves branches vulnerable to infection.'],
                       'nutrient_guidance': None,
                       'prevention': ['Remove dead wood and fruit mummies during orchard '
                                      'sanitation before periods favorable for infection.',
                                      'Protect pruning and other wounds according to locally '
                                      'recommended orchard practices.',
                                      'Maintain balanced tree growth and reduce avoidable stress '
                                      'or sun injury that can create infection sites.'],
                       'review_status': 'REQUIRES_SOURCE_REVIEW',
                       'sources': [{'organization': 'University of Minnesota Extension',
                                    'title': 'Apple leaf and fruit disease diagnosis',
                                    'url': 'https://apps.extension.umn.edu/garden/diagnose/plant/deciduous/apple/leavesspots.html'}],
                       'spread': ['The fungus survives in dead wood, cankers, mummified fruit and '
                                  'other infected plant material.',
                                  'Spores are released from these sources during wet weather and '
                                  'can be spread by rain splash.',
                                  'Wounds and stressed or dead tissues provide important infection '
                                  'sites.'],
                       'symptoms': ['Purple-flecked leaf spots enlarge into circular lesions with '
                                    'tan centers.',
                                    'Fruit can develop small brown areas that enlarge into dark, '
                                    'sunken rots.',
                                    'Dead or weakened limbs and mummified fruit can remain as '
                                    'sources of infection.'],
                       'treatment_note': 'Management focuses strongly on sanitation and protection '
                                         'of susceptible tissues; chemical treatment is not '
                                         'prescribed here.',
                       'type': 'Fungal Disease'},
 'Apple___Cedar_apple_rust': {'causal_agent': 'Gymnosporangium juniperi-virginianae',
                              'chemical_treatment': None,
                              'condition': 'Cedar-apple rust',
                              'crop': 'Apple',
                              'diagnostic_caution': 'The model predicts a dataset label from an '
                                                    'image; it does not confirm the pathogen, '
                                                    'distinguish all look-alike conditions, or '
                                                    'assess disease severity. Confirm uncertain '
                                                    'cases with a qualified plant-health '
                                                    'professional.',
                              'management': ['Inspect nearby eastern red cedar or susceptible '
                                             'juniper plants for rust galls and manage infected '
                                             'alternate hosts where practical.',
                                             'Monitor apple foliage during wet spring periods when '
                                             'spores from juniper/cedar can initiate infection.',
                                             'Remove severely affected apple material when '
                                             'appropriate, while recognizing that removing only '
                                             'apple tissue does not eliminate the alternate-host '
                                             'source.'],
                              'nutrient_guidance': None,
                              'prevention': ['Avoid establishing susceptible apple and '
                                             'juniper/cedar hosts in close proximity where '
                                             'cedar-apple rust is a recurring problem.',
                                             'Choose rust-resistant apple cultivars where '
                                             'available.',
                                             'Reduce nearby sources of rust galls on susceptible '
                                             'juniper or cedar plants.'],
                              'review_status': 'REQUIRES_SOURCE_REVIEW',
                              'sources': [{'organization': 'University of Minnesota Extension',
                                           'title': 'Cedar-Apple Rust',
                                           'url': 'https://apps.extension.umn.edu/garden/diagnose/plant/fruit/apple/leavesspots.html'}],
                              'spread': ['The pathogen requires compatible juniper or cedar hosts '
                                         'to complete its disease cycle.',
                                         'Spores produced on infected juniper/cedar structures can '
                                         'reach susceptible apple tissue, especially during wet '
                                         'spring weather.',
                                         'Rain and wind assist movement of spores between the '
                                         'alternate hosts.'],
                              'symptoms': ['Apple leaves develop yellow to bright-orange spots, '
                                           'often with reddish margins.',
                                           'Small dark structures may appear on the upper leaf '
                                           'surface and fringed structures can develop beneath '
                                           'lesions.',
                                           'Fruit may develop rough green-to-brown irregular '
                                           'lesions.'],
                              'treatment_note': 'The key preventive approach is disrupting the '
                                                'apple–juniper/cedar disease cycle; no chemical '
                                                'treatment is prescribed here.',
                              'type': 'Fungal Disease'},
 'Apple___healthy': {'causal_agent': None,
                     'chemical_treatment': None,
                     'condition': 'healthy',
                     'crop': 'Apple',
                     'diagnostic_caution': 'A healthy prediction is a model classification, not a '
                                           'guarantee that the plant is disease-free.',
                     'management': ['Continue routine crop monitoring and follow locally '
                                    'recommended agronomic practices.',
                                    'If symptoms are visible despite this prediction, obtain a '
                                    'second assessment; the classifier can miss conditions.'],
                     'nutrient_guidance': None,
                     'prevention': ['Use clean planting material, maintain appropriate spacing and '
                                    'irrigation, and monitor plants regularly.'],
                     'review_status': 'REQUIRES_SOURCE_REVIEW',
                     'sources': [],
                     'spread': ['Not applicable to a healthy-class prediction.'],
                     'symptoms': ['The classifier assigned the healthy class. This is not a '
                                  'guarantee that the whole plant is free from disease, pests, or '
                                  'nutrient stress.'],
                     'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                       'prediction.',
                     'type': 'healthy'},
 'Banana___Bract_Mosaic_Virus': {'causal_agent': 'Banana bract mosaic virus (potyvirus)',
                                 'chemical_treatment': None,
                                 'condition': 'Banana bract mosaic virus',
                                 'crop': 'Banana',
                                 'diagnostic_caution': 'This is an image-classification result, '
                                                       'not a confirmed field diagnosis. Similar '
                                                       'symptoms can have different causes; '
                                                       'confirm with a qualified plant pathologist '
                                                       'or local agricultural extension service '
                                                       'before high-impact action. The prediction '
                                                       'is not a confirmed field diagnosis; '
                                                       'look-alike biotic and abiotic causes may '
                                                       'require examination or laboratory testing.',
                                 'management': ['Remove and destroy plants showing characteristic '
                                                'bract-mosaic symptoms to reduce field sources.',
                                                'Use virus-free planting material for new '
                                                'plantings and inspect suckers before '
                                                'establishment.',
                                                'Inspect fields regularly for early symptoms and '
                                                'manage aphid populations according to locally '
                                                'approved guidance.'],
                                 'nutrient_guidance': None,
                                 'prevention': ['Start new plantings with certified or '
                                                'disease-free banana planting material.',
                                                'Rogue symptomatic plants promptly rather than '
                                                'allowing them to remain as virus sources.',
                                                'Control weeds and volunteer banana plants around '
                                                'production areas where they can support vectors '
                                                'or disease spread.'],
                                 'review_status': 'REQUIRES_SOURCE_REVIEW',
                                 'sources': [{'organization': 'TNAU Agritech Portal',
                                              'title': 'Banana Bract Virus',
                                              'url': 'https://agritech.tnau.ac.in/crop_protection/banana_diseases/crop_prot_crop%20diseases_fruits_banana_2.html'}],
                                 'spread': ['The virus is primarily spread through infected '
                                            'suckers or other vegetative planting material.',
                                            'Aphids, including Aphis gossypii and Rhopalosiphum '
                                            'maidis, can transmit the virus between plants.',
                                            'Infected volunteer or neglected banana plants can '
                                            'maintain a source of virus in the field.'],
                                 'symptoms': ['Pink to reddish spindle-shaped streaks occur on the '
                                              'pseudostem, midrib and peduncle.',
                                              'Mosaic or spindle-shaped streaks can appear on '
                                              'bracts, peduncles and fingers.',
                                              'Infected suckers may show reddish-brown streaks and '
                                              'plants can develop abnormal crown growth and poorly '
                                              'filled hands.'],
                                 'treatment_note': 'There is no curative treatment in this '
                                                   'knowledge base for an established viral '
                                                   'infection; management focuses on clean '
                                                   'planting material, early detection and removal '
                                                   'of infected plants.',
                                 'type': 'Viral Disease'},
 'Banana___Cordana': {'causal_agent': 'Cordana musae',
                      'chemical_treatment': None,
                      'condition': 'Cordana leaf spot',
                      'crop': 'Banana',
                      'diagnostic_caution': 'The model predicts a dataset label from an image; it '
                                            'does not confirm Cordana musae, distinguish all '
                                            'look-alike leaf spots, or assess disease severity.',
                      'management': ['Remove heavily infected leaves where practical to reduce '
                                     'visible sources of spores.',
                                     'Monitor leaf lesions and avoid practices that maintain '
                                     'prolonged wetness around the banana canopy.',
                                     'Because Cordana may colonize pre-existing leaf lesions, '
                                     'assess other leaf-spot symptoms rather than assuming Cordana '
                                     'is the only cause.'],
                      'nutrient_guidance': None,
                      'prevention': ['Maintain field drainage and spacing that help foliage dry '
                                     'after rain.',
                                     'Inspect leaves regularly for the characteristic oval or '
                                     'diamond-shaped lesions and greyish-brown sporulation.',
                                     'Remove heavily diseased leaf material where locally '
                                     'appropriate; do not infer a fungicide treatment from the '
                                     'image label.'],
                      'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                      'sources': [{'organization': 'Pacific Pests, Pathogens & Weeds (Lucid)',
                                   'title': 'Banana diamond leaf spot (Cordana musae)',
                                   'url': 'https://apps.lucidcentral.org/ppp_v9/text/web_mini/entities/banana_diamond_leaf_spot_072.htm'},
                                  {'organization': 'Crop Science Australia',
                                   'title': 'Cordana leaf spot',
                                   'url': 'https://www.crop.bayer.com.au/crop-management/diseases/cordana-leaf-spot'}],
                      'spread': ['Spores are produced on affected leaves, including the lower leaf '
                                 'surface.',
                                 'Spores can disperse in wet, windy weather; frequent rain and '
                                 'hot, humid conditions favor disease development.',
                                 'Cordana leaf spot may occur on or around lesions caused by other '
                                 'leaf-spot fungi and can behave as a secondary invader.'],
                      'symptoms': ['Oval to diamond-shaped pale-brown leaf spots, often with '
                                   'yellow margins, can develop on banana leaves.',
                                   'Lesions may show concentric zonation and can enlarge or merge, '
                                   'especially along leaf margins.',
                                   'The underside of affected areas may develop greyish-brown, '
                                   'hairy sporulation; extensive lesions can dry large areas of '
                                   'the leaf.'],
                      'treatment_note': 'No chemical treatment is prescribed by this educational '
                                        'knowledge base; management emphasizes sanitation and '
                                        'reduction of prolonged leaf wetness.',
                      'type': 'Fungal Disease'},
 'Banana___Insect_Pest': {'causal_agent': None,
                          'chemical_treatment': None,
                          'condition': 'Insect pest damage (class label)',
                          'crop': 'Banana',
                          'diagnostic_caution': 'This is a broad insect-pest class. Banana has '
                                                'several unrelated insect pests, and their '
                                                'symptoms differ. The model cannot identify the '
                                                'insect species or establish that a particular '
                                                'symptom was caused by an insect; inspect the '
                                                'plant and obtain field confirmation. The '
                                                'prediction is not a confirmed field diagnosis; '
                                                'look-alike biotic and abiotic causes may require '
                                                'examination or laboratory testing.',
                          'management': ['Inspect the affected plant closely for the actual insect '
                                         'or characteristic feeding signs before selecting a '
                                         'control measure.',
                                         'Record where damage occurs—young leaves, pseudostem, '
                                         'corm, roots or fruit—to narrow the pest identity.',
                                         'Use integrated pest management: monitoring, sanitation, '
                                         'conservation of natural enemies and only crop- and '
                                         'pest-specific controls that are locally recommended.'],
                          'nutrient_guidance': None,
                          'prevention': ['Use healthy planting material and inspect new plants '
                                         'before introducing them to the field.',
                                         'Remove heavily infested plant material when appropriate '
                                         'and keep production areas free of unnecessary plant '
                                         'debris.',
                                         'Do not apply a pesticide solely from the model label '
                                         'because this class does not identify the pest species.'],
                          'review_status': 'REQUIRES_SOURCE_REVIEW',
                          'sources': [{'organization': 'TNAU Agritech Portal',
                                       'title': 'Banana Crop Protection',
                                       'url': 'https://www.agritech.tnau.ac.in/expert_system/banana/cropprotection.html'}],
                          'spread': ['The specific mode of spread cannot be determined from the '
                                     "broad 'Insect_Pest' class label alone.",
                                     'Insect populations can increase through local reproduction '
                                     'and may move between neighboring banana plants or fields.'],
                          'symptoms': ['Visible feeding injury may include leaf scraping, holes, '
                                       'curling, discoloration, wilting or damage concentrated '
                                       'around young leaves and shoots.',
                                       'The exact appearance depends on the insect species, plant '
                                       'part attacked and feeding stage.'],
                          'treatment_note': 'Because the model class is intentionally broad, a '
                                            'specific insecticide or treatment cannot be safely '
                                            'recommended from this prediction alone. Confirm the '
                                            'pest species first.',
                          'type': 'Insect Pest'},
 'Banana___Moko': {'causal_agent': 'Ralstonia solanacearum',
                   'chemical_treatment': None,
                   'condition': 'Moko disease',
                   'crop': 'Banana',
                   'diagnostic_caution': 'The model predicts a dataset label from an image; it '
                                         'does not confirm the pathogen, distinguish all '
                                         'look-alike conditions, or assess disease severity. '
                                         'Confirm uncertain cases with a qualified plant-health '
                                         'professional.',
                   'management': ['Remove confirmed infected plants and manage surrounding '
                                  'contaminated material according to local plant-health guidance.',
                                  'Clean and disinfect cutting tools after work on suspect or '
                                  'infected plants.',
                                  'Restrict movement of soil, water, tools and planting material '
                                  'from affected areas to clean fields.'],
                   'nutrient_guidance': None,
                   'prevention': ['Use pathogen-free planting material from reliable sources.',
                                  'Keep machinery, footwear and cutting tools from moving '
                                  'contaminated soil or plant residues into clean blocks.',
                                  'Inspect plants regularly so suspect wilted plants can be '
                                  'isolated and investigated early.'],
                   'review_status': 'REQUIRES_SOURCE_REVIEW',
                   'sources': [{'organization': 'TNAU Agritech Portal',
                                'title': 'Banana Crop Protection',
                                'url': 'https://www.agritech.tnau.ac.in/expert_system/banana/cropprotection.html'}],
                   'spread': ['The bacterium can move through infected planting material and '
                              'contaminated soil or water.',
                              'Farm tools and movement of soil or plant material can transfer the '
                              'pathogen between plants.',
                              'Insects and other agents that contact infected plant tissues can '
                              'contribute to local spread in some production systems.'],
                   'symptoms': ['Plants can develop rapid yellowing and wilting of leaves.',
                                'Internal vascular tissues may show brown to reddish-brown '
                                'discoloration when affected pseudostem or rhizome tissue is '
                                'examined.',
                                'Fruit and bunch development may be abnormal in severely affected '
                                'plants.'],
                   'treatment_note': 'There is no curative treatment recommended here for an '
                                     'established systemic bacterial infection; containment, '
                                     'sanitation and clean planting material are the key measures.',
                   'type': 'Bacterial Disease'},
 'Banana___Panama': {'causal_agent': 'Fusarium oxysporum f. sp. cubense',
                     'chemical_treatment': None,
                     'condition': 'Panama disease / Fusarium wilt',
                     'crop': 'Banana',
                     'diagnostic_caution': 'This is an image-classification result, not a '
                                           'confirmed field diagnosis. Similar symptoms can have '
                                           'different causes; confirm with a qualified plant '
                                           'pathologist or local agricultural extension service '
                                           'before high-impact action. The prediction is not a '
                                           'confirmed field diagnosis; look-alike biotic and '
                                           'abiotic causes may require examination or laboratory '
                                           'testing.',
                     'management': ['Isolate affected areas and avoid moving soil, tools or '
                                    'machinery from infested to clean fields.',
                                    'Remove severely affected plants according to local '
                                    'plant-health guidance rather than replanting immediately into '
                                    'contaminated spots.',
                                    'Use resistant or tolerant cultivars appropriate to the '
                                    'Fusarium race and production region when available.'],
                     'nutrient_guidance': None,
                     'prevention': ['Use disease-free planting material and maintain strict field '
                                    'sanitation.',
                                    'Clean and disinfect tools, footwear and machinery before '
                                    'moving between fields.',
                                    'Avoid introducing soil or planting material from known '
                                    'Panama-disease sites.'],
                     'review_status': 'REQUIRES_SOURCE_REVIEW',
                     'sources': [{'organization': 'TNAU Agritech Portal',
                                  'title': 'Panama Wilt of Banana',
                                  'url': 'https://agritech.tnau.ac.in/expert_system/banana/cropprotection.html'}],
                     'spread': ['The pathogen persists in infested soil and can be moved with '
                                'contaminated planting material, soil, water, tools and machinery.',
                                'Root infection allows the fungus to colonize the vascular system '
                                'of the plant.',
                                'Movement of contaminated soil or planting material can introduce '
                                'the disease into previously clean fields.'],
                     'symptoms': ['Lower leaves yellow and wilt, often progressing upward as the '
                                  'disease becomes severe.',
                                  'The plant can develop a spiky appearance as dead lower leaves '
                                  'hang around the pseudostem.',
                                  'Cutting affected rhizome or pseudostem tissue can reveal '
                                  'reddish-brown to maroon vascular discoloration.'],
                     'treatment_note': 'Because the pathogen survives in soil and colonizes plant '
                                       'vascular tissue, the emphasis is on exclusion, sanitation '
                                       'and resistant planting material rather than a curative '
                                       'foliar treatment.',
                     'type': 'Fungal Disease'},
 'Banana___Pestalotiopsis': {'causal_agent': 'Pestalotiopsis palmarum',
                             'chemical_treatment': None,
                             'condition': 'Pestalotiopsis leaf spot',
                             'crop': 'Banana',
                             'diagnostic_caution': 'The dataset label is Pestalotiopsis leaf spot, '
                                                   'and an image prediction is not laboratory '
                                                   'confirmation of the causal species. APS lists '
                                                   'Pestalotiopsis palmarum for banana '
                                                   'Pestalotiopsis leaf spot, but similar '
                                                   'leaf-blight symptoms can have other fungal '
                                                   'causes. Confirm uncertain cases with a '
                                                   'qualified plant-health professional or '
                                                   'laboratory.',
                             'management': ['Remove heavily infected or dead leaves where '
                                            'practical to reduce inoculum.',
                                            'Improve canopy ventilation and avoid prolonged leaf '
                                            'wetness from irrigation practices.',
                                            'Monitor expanding lesions on older leaves and prevent '
                                            'infected debris from accumulating around plants.'],
                             'nutrient_guidance': None,
                             'prevention': ['Use clean planting material and avoid transporting '
                                            'visibly infected leaf debris.',
                                            'Maintain spacing and drainage that reduce prolonged '
                                            'humidity around foliage.',
                                            'Combine sanitation with regular scouting so expanding '
                                            'leaf lesions are detected early.'],
                             'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                             'sources': [{'organization': 'TNAU Agritech Portal',
                                          'title': 'Banana Crop Protection',
                                          'url': 'https://www.agritech.tnau.ac.in/expert_system/banana/cropprotection.html'},
                                         {'organization': 'American Phytopathological Society '
                                                          '(APS)',
                                          'title': 'Diseases of Banana and Plantain — '
                                                   'Pestalotiopsis leaf spot',
                                          'url': 'https://www.apsnet.org/edcenter/resources/commonnames/Pages/BananaandPlantain.aspx'}],
                             'spread': ['Spores from infected leaves and plant debris can spread '
                                        'during humid or wet conditions.',
                                        'Rain splash and movement of contaminated plant material '
                                        'can move fungal inoculum between plants.',
                                        'Dense, humid canopies favor persistence and secondary '
                                        'spread of leaf-spot fungi.'],
                             'symptoms': ['Leaf lesions begin as small spots and enlarge into '
                                          'brown to dark necrotic areas.',
                                          'Older lesions may develop pale or gray centers with '
                                          'darker margins and can merge under severe infection.',
                                          'Extensive leaf damage reduces photosynthetic area and '
                                          'may lead to premature leaf drying.'],
                             'treatment_note': 'No chemical treatment is prescribed here; the '
                                               'knowledge base emphasizes sanitation, airflow and '
                                               'reduction of prolonged leaf wetness.',
                             'type': 'Fungal Disease'},
 'Banana___Sigatoka': {'causal_agent': 'Sigatoka leaf-spot complex (Pseudocercospora spp.; exact '
                                       'species not identifiable from this generic class)',
                       'chemical_treatment': None,
                       'condition': 'Sigatoka leaf spot',
                       'crop': 'Banana',
                       'diagnostic_caution': 'This is a broad Sigatoka-class prediction. Banana '
                                             'Sigatoka leaf diseases include yellow Sigatoka '
                                             '(Pseudocercospora musae), black Sigatoka (P. '
                                             'fijiensis), and Eumusae leaf spot (P. eumusae). '
                                             'Their symptoms can overlap, and this classifier does '
                                             'not identify the species or confirm the pathogen. '
                                             'Field or laboratory confirmation is required for a '
                                             'definitive diagnosis.',
                       'management': ['Remove and destroy severely affected leaves to reduce the '
                                      'amount of fungal inoculum in the plantation.',
                                      'Avoid excessively close spacing and improve drainage so '
                                      'foliage dries more rapidly.',
                                      'Scout regularly for the earliest leaf streaks and manage '
                                      'the disease before extensive defoliation occurs.'],
                       'nutrient_guidance': None,
                       'prevention': ['Maintain adequate spacing and field drainage to limit '
                                      'prolonged leaf wetness.',
                                      'Remove infected leaves and old diseased debris instead of '
                                      'allowing them to accumulate.',
                                      'Use healthy planting material and avoid establishing new '
                                      'plants from heavily diseased sources.'],
                       'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                       'sources': [{'organization': 'American Phytopathological Society (APS)',
                                    'title': 'The Vulnerability of Bananas to Globally Emerging '
                                             'Disease Threats — Sigatoka',
                                    'url': 'https://apsjournals.apsnet.org/doi/full/10.1094/PHYTO-07-20-0311-RVW'},
                                   {'organization': 'Studies in Mycology',
                                    'title': 'Pseudocercospora and allied genera associated with '
                                             'leaf spots of banana',
                                    'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8165963/'}],
                       'spread': ['Fungal spores spread from infected leaves during humid and wet '
                                  'conditions.',
                                  'Rain splash and airborne movement of spores can carry inoculum '
                                  'to nearby leaves.',
                                  'Disease development is favored by prolonged leaf wetness and '
                                  'dense foliage.'],
                       'symptoms': ['Small pale streaks or spots develop on leaves and expand into '
                                    'brown lesions.',
                                    'Older lesions can develop gray centers and yellow halos.',
                                    'Severe disease causes rapid leaf drying and defoliation, '
                                    'reducing the healthy leaf area needed for bunch development.'],
                       'treatment_note': 'The main management targets are infected foliage, canopy '
                                         'humidity and early detection. No chemical treatment is '
                                         'prescribed by this knowledge base.',
                       'type': 'Fungal Disease'},
 'Banana___Yellow_Sigatoka': {'causal_agent': 'Pseudocercospora musae (syn. Mycosphaerella '
                                              'musicola)',
                              'chemical_treatment': None,
                              'condition': 'Yellow Sigatoka',
                              'crop': 'Banana',
                              'diagnostic_caution': 'This is an image-classification result, not a '
                                                    'confirmed field diagnosis. Similar symptoms '
                                                    'can have different causes; confirm with a '
                                                    'qualified plant pathologist or local '
                                                    'agricultural extension service before '
                                                    'high-impact action. The prediction is not a '
                                                    'confirmed field diagnosis; look-alike biotic '
                                                    'and abiotic causes may require examination or '
                                                    'laboratory testing.',
                              'management': ['Remove and destroy affected leaves to lower the '
                                             'amount of inoculum available for new infections.',
                                             'Avoid close spacing and correct drainage problems '
                                             'that keep banana foliage wet for long periods.',
                                             'Scout for the first pale streaks and intervene '
                                             'before lesions coalesce and cause extensive '
                                             'defoliation.'],
                              'nutrient_guidance': None,
                              'prevention': ['Maintain adequate plant spacing and drainage to '
                                             'reduce prolonged leaf wetness.',
                                             'Keep the plantation free of heavily infected leaf '
                                             'debris and remove affected leaves promptly.',
                                             'Use healthy planting material and maintain adequate '
                                             'functional green leaves for bunch development.'],
                              'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                              'sources': [{'organization': 'TNAU Agritech Portal',
                                           'title': 'Yellow Sigatoka of Banana',
                                           'url': 'https://agritech.tnau.ac.in/crop_protection/banana_diseases/crop_prot_crop%20diseases_fruits_banana_8.html'},
                                          {'organization': 'American Phytopathological Society '
                                                           '(APS)',
                                           'title': 'The Vulnerability of Bananas to Globally '
                                                    'Emerging Disease Threats — Yellow Sigatoka',
                                           'url': 'https://apsjournals.apsnet.org/doi/full/10.1094/PHYTO-07-20-0311-RVW'}],
                              'spread': ['Spores produced on infected foliage can spread to '
                                         'healthy banana leaves under favorable humid and wet '
                                         'conditions.',
                                         'Rain and wind-assisted movement of spores can distribute '
                                         'inoculum within a plantation.',
                                         'Dense foliage and prolonged leaf wetness increase the '
                                         'opportunity for infection.'],
                              'symptoms': ['Pale yellow or greenish streaks appear parallel to '
                                           'leaf veins.',
                                           'Streaks enlarge into elliptical brown spots with gray '
                                           'centers and yellow halos.',
                                           'Lesions can merge into large dried areas, followed by '
                                           'rapid leaf drying and defoliation.'],
                              'treatment_note': 'No chemical treatment is prescribed here; the '
                                                'disease-specific emphasis is on infected-leaf '
                                                'removal, canopy conditions and early detection.',
                              'type': 'Fungal Disease'},
 'Banana___healthy': {'causal_agent': None,
                      'chemical_treatment': None,
                      'condition': 'healthy',
                      'crop': 'Banana',
                      'diagnostic_caution': 'A healthy prediction is a model classification, not a '
                                            'guarantee that the plant is disease-free.',
                      'management': ['Continue routine crop monitoring and follow locally '
                                     'recommended agronomic practices.',
                                     'If symptoms are visible despite this prediction, obtain a '
                                     'second assessment; the classifier can miss conditions.'],
                      'nutrient_guidance': None,
                      'prevention': ['Use clean planting material, maintain appropriate spacing '
                                     'and irrigation, and monitor plants regularly.'],
                      'review_status': 'REQUIRES_SOURCE_REVIEW',
                      'sources': [],
                      'spread': ['Not applicable to a healthy-class prediction.'],
                      'symptoms': ['The classifier assigned the healthy class. This is not a '
                                   'guarantee that the whole plant is free from disease, pests, or '
                                   'nutrient stress.'],
                      'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                        'prediction.',
                      'type': 'healthy'},
 'Blueberry___healthy': {'causal_agent': None,
                         'chemical_treatment': None,
                         'condition': 'healthy',
                         'crop': 'Blueberry',
                         'diagnostic_caution': 'A healthy prediction is a model classification, '
                                               'not a guarantee that the plant is disease-free.',
                         'management': ['Continue routine crop monitoring and follow locally '
                                        'recommended agronomic practices.',
                                        'If symptoms are visible despite this prediction, obtain a '
                                        'second assessment; the classifier can miss conditions.'],
                         'nutrient_guidance': None,
                         'prevention': ['Use clean planting material, maintain appropriate spacing '
                                        'and irrigation, and monitor plants regularly.'],
                         'review_status': 'REQUIRES_SOURCE_REVIEW',
                         'sources': [],
                         'spread': ['Not applicable to a healthy-class prediction.'],
                         'symptoms': ['The classifier assigned the healthy class. This is not a '
                                      'guarantee that the whole plant is free from disease, pests, '
                                      'or nutrient stress.'],
                         'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                           'prediction.',
                         'type': 'healthy'},
 'Cauliflower___Black_Rot': {'causal_agent': 'Xanthomonas campestris pv. campestris',
                             'chemical_treatment': None,
                             'condition': 'Cauliflower black rot',
                             'crop': 'Cauliflower',
                             'diagnostic_caution': 'This is an image-classification result, not a '
                                                   'confirmed field diagnosis. Similar symptoms '
                                                   'can have different causes; confirm with a '
                                                   'qualified plant pathologist or local '
                                                   'agricultural extension service before '
                                                   'high-impact action. The prediction is not a '
                                                   'confirmed field diagnosis; look-alike biotic '
                                                   'and abiotic causes may require examination or '
                                                   'laboratory testing.',
                             'management': ['Use healthy, tested seed and disease-free '
                                            'transplants.',
                                            'Remove infected crop residues and avoid working among '
                                            'wet plants.',
                                            'Rotate away from brassica crops and clean trays and '
                                            'tools between uses.'],
                             'nutrient_guidance': None,
                             'prevention': ['Use clean seed and healthy nursery material.',
                                            'Maintain field sanitation and avoid overhead '
                                            'irrigation where practical.'],
                             'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                             'sources': [{'organization': 'TNAU Agritech Portal',
                                          'title': 'Black rot of crucifers: symptoms and '
                                                   'management',
                                          'url': 'https://agritech.tnau.ac.in/org_farm/orgfarm_hortidiseases.html'},
                                         {'organization': 'TNAU Agritech Portal',
                                          'title': 'IPM schedule for vegetables: bacterial black '
                                                   'rot',
                                          'url': 'https://agritech.tnau.ac.in/horticulture/pdf/tech_bulletin/national/IPM-Schedule-for-vegetables.pdf'}],
                             'spread': ['The bacterium can be seedborne and can spread through '
                                        'infected transplants, water splash and contaminated '
                                        'tools.'],
                             'symptoms': ['Yellow, V-shaped lesions may begin at leaf margins and '
                                          'extend towards the midrib.',
                                          'Veins within affected areas may darken; severe '
                                          'infection can cause leaf blight and curd '
                                          'discoloration.'],
                             'treatment_note': 'No chemical treatment is prescribed by this '
                                               'educational entry. Confirm the condition and '
                                               'consult current local agricultural-extension '
                                               'guidance and the applicable product label before '
                                               'considering any crop-protection product.',
                             'type': 'bacterial_disease'},
 'Cauliflower___Downy_Mildew': {'causal_agent': 'Peronospora parasitica (older taxonomic usage; '
                                                'downy mildew pathogen complex)',
                                'chemical_treatment': None,
                                'condition': 'Cauliflower downy mildew',
                                'crop': 'Cauliflower',
                                'diagnostic_caution': 'This is an image-classification result, not '
                                                      'a confirmed field diagnosis. Similar '
                                                      'symptoms can have different causes; confirm '
                                                      'with a qualified plant pathologist or local '
                                                      'agricultural extension service before '
                                                      'high-impact action. The prediction is not a '
                                                      'confirmed field diagnosis; look-alike '
                                                      'biotic and abiotic causes may require '
                                                      'examination or laboratory testing.',
                                'management': ['Use healthy transplants and remove heavily '
                                               'infected plant debris.',
                                               'Improve spacing, airflow and drainage.',
                                               'Avoid prolonged leaf wetness and seek local '
                                               'extension guidance if the disease spreads.'],
                                'nutrient_guidance': None,
                                'prevention': ['Maintain nursery hygiene and rotate crops where '
                                               'practical.',
                                               'Monitor seedlings and leaves during cool, humid '
                                               'weather.'],
                                'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                                'sources': [{'organization': 'TNAU Agritech Portal',
                                             'title': 'Downy mildew of cauliflower: symptoms and '
                                                      'management',
                                             'url': 'https://agritech.tnau.ac.in/crop_protection/cauliflower_disease_1.html'}],
                                'spread': ['Downy mildew is favoured by humid conditions and leaf '
                                           'wetness; spores can spread between plants.'],
                                'symptoms': ['Yellow or pale patches may develop on leaves; downy '
                                             'growth may be visible on the lower leaf surface in '
                                             'humid conditions.',
                                             'Curds may develop superficial discoloured spots, '
                                             'reducing marketability.'],
                                'treatment_note': 'No chemical treatment is prescribed by this '
                                                  'educational entry. Confirm the condition and '
                                                  'consult current local agricultural-extension '
                                                  'guidance and the applicable product label '
                                                  'before considering any crop-protection product.',
                                'type': 'oomycete_or_downy_mildew'},
 'Cauliflower___healthy': {'causal_agent': None,
                           'chemical_treatment': None,
                           'condition': 'healthy',
                           'crop': 'Cauliflower',
                           'diagnostic_caution': 'A healthy prediction is a model classification, '
                                                 'not a guarantee that the plant is disease-free.',
                           'management': ['Continue routine crop monitoring and follow locally '
                                          'recommended agronomic practices.',
                                          'If symptoms are visible despite this prediction, obtain '
                                          'a second assessment; the classifier can miss '
                                          'conditions.'],
                           'nutrient_guidance': None,
                           'prevention': ['Use clean planting material, maintain appropriate '
                                          'spacing and irrigation, and monitor plants regularly.'],
                           'review_status': 'REQUIRES_SOURCE_REVIEW',
                           'sources': [],
                           'spread': ['Not applicable to a healthy-class prediction.'],
                           'symptoms': ['The classifier assigned the healthy class. This is not a '
                                        'guarantee that the whole plant is free from disease, '
                                        'pests, or nutrient stress.'],
                           'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                             'prediction.',
                           'type': 'healthy'},
 'Cherry_(including_sour)___Powdery_mildew': {'causal_agent': 'Podosphaera clandestina',
                                              'chemical_treatment': None,
                                              'condition': 'Cherry powdery mildew',
                                              'crop': 'Cherry',
                                              'diagnostic_caution': 'The model predicts a dataset '
                                                                    'label from an image; it does '
                                                                    'not confirm the pathogen, '
                                                                    'distinguish all look-alike '
                                                                    'conditions, or assess disease '
                                                                    'severity.',
                                              'management': ['Monitor young shoots and leaves '
                                                             'closely during periods favorable for '
                                                             'powdery mildew rather than waiting '
                                                             'for severe leaf distortion.',
                                                             'Prune appropriately to improve light '
                                                             'penetration and airflow through the '
                                                             'canopy.',
                                                             'Remove severely affected plant '
                                                             'material where practical and avoid '
                                                             'excessive vegetative growth that '
                                                             'creates a dense canopy.'],
                                              'nutrient_guidance': None,
                                              'prevention': ['Maintain an open canopy so young '
                                                             'tissues receive adequate light and '
                                                             'airflow.',
                                                             'Avoid excessive nitrogen-driven '
                                                             'vegetative growth that produces '
                                                             'dense, highly susceptible shoots.',
                                                             'Use locally adapted, '
                                                             'less-susceptible cultivars where '
                                                             'available.'],
                                              'review_status': 'REQUIRES_SOURCE_REVIEW',
                                              'sources': [{'organization': 'TNAU Agritech Portal',
                                                           'title': 'Cherry disease-management '
                                                                    'bulletin',
                                                           'url': 'https://agritech.tnau.ac.in/crop_protection/crop_pdf/Cherry.pdf'}],
                                              'spread': ['Powdery mildew spores are dispersed '
                                                         'through the air from infected tissues.',
                                                         'The pathogen can persist on infected '
                                                         'plant material and initiate new '
                                                         'infections during favorable weather.',
                                                         'Unlike many leaf-spot diseases, free '
                                                         'water on leaves is not required for '
                                                         'spore germination; humid conditions can '
                                                         'still favor disease development.'],
                                              'symptoms': ['White powdery fungal growth develops '
                                                           'on young leaves, shoots or other '
                                                           'susceptible green tissues.',
                                                           'Affected leaves may become distorted, '
                                                           'curled or discolored as infection '
                                                           'progresses.',
                                                           'Young fruit or shoots can be affected '
                                                           'when disease pressure is high.'],
                                              'treatment_note': 'Treatment decisions should be '
                                                                'based on local cherry production '
                                                                'guidance and disease pressure; no '
                                                                'chemical treatment is prescribed '
                                                                'here.',
                                              'type': 'Fungal Disease'},
 'Cherry_(including_sour)___healthy': {'causal_agent': None,
                                       'chemical_treatment': None,
                                       'condition': 'healthy',
                                       'crop': 'Cherry',
                                       'diagnostic_caution': 'A healthy prediction is a model '
                                                             'classification, not a guarantee that '
                                                             'the plant is disease-free.',
                                       'management': ['Continue routine crop monitoring and follow '
                                                      'locally recommended agronomic practices.',
                                                      'If symptoms are visible despite this '
                                                      'prediction, obtain a second assessment; the '
                                                      'classifier can miss conditions.'],
                                       'nutrient_guidance': None,
                                       'prevention': ['Use clean planting material, maintain '
                                                      'appropriate spacing and irrigation, and '
                                                      'monitor plants regularly.'],
                                       'review_status': 'REQUIRES_SOURCE_REVIEW',
                                       'sources': [],
                                       'spread': ['Not applicable to a healthy-class prediction.'],
                                       'symptoms': ['The classifier assigned the healthy class. '
                                                    'This is not a guarantee that the whole plant '
                                                    'is free from disease, pests, or nutrient '
                                                    'stress.'],
                                       'treatment_note': 'No disease treatment is indicated by a '
                                                         'healthy-class prediction.',
                                       'type': 'healthy'},
 'Chilli___Anthracnose': {'causal_agent': 'Colletotrichum capsici (TNAU identification; '
                                          'Colletotrichum species complex may occur)',
                          'chemical_treatment': None,
                          'condition': 'Chilli anthracnose / fruit rot',
                          'crop': 'Chilli',
                          'diagnostic_caution': 'This is an image-classification result, not a '
                                                'confirmed field diagnosis. Similar symptoms can '
                                                'have different causes; confirm with a qualified '
                                                'plant pathologist or local agricultural extension '
                                                'service before high-impact action. The prediction '
                                                'is not a confirmed field diagnosis; look-alike '
                                                'biotic and abiotic causes may require examination '
                                                'or laboratory testing.',
                          'management': ['Use disease-free seed and remove infected fruits and '
                                         'crop debris.',
                                         'Avoid overhead irrigation and handling wet plants.',
                                         'Maintain adequate spacing and seek local diagnosis if '
                                         'symptoms differ from typical fruit lesions.'],
                          'nutrient_guidance': None,
                          'prevention': ['Use healthy seed and maintain field sanitation.',
                                         'Monitor fruit development during humid and rainy '
                                         'periods.'],
                          'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                          'sources': [{'organization': 'TNAU Agritech Portal',
                                       'title': 'Chilli anthracnose: symptoms, pathogen and '
                                                'management',
                                       'url': 'https://agritech.tnau.ac.in/crop_protection/chilli_phdiseases_2.html'}],
                          'spread': ['The pathogen may be seedborne; spores can spread through air '
                                     'and rain splash, especially in warm, humid weather.'],
                          'symptoms': ['Small, dark, circular spots may develop on ripening chilli '
                                       'fruits.',
                                       'Severely affected fruits may become pale, shrivelled or '
                                       'rotten; pinkish spore masses may occur under humid '
                                       'conditions.'],
                          'treatment_note': 'No chemical treatment is prescribed by this '
                                            'educational entry. Confirm the condition and consult '
                                            'current local agricultural-extension guidance and the '
                                            'applicable product label before considering any '
                                            'crop-protection product.',
                          'type': 'fungal_disease'},
 'Chilli___Leaf_Curl': {'causal_agent': 'Leaf-curl-associated begomoviruses may be involved; exact '
                                        'virus requires laboratory confirmation',
                        'chemical_treatment': None,
                        'condition': 'Chilli leaf curl syndrome',
                        'crop': 'Chilli',
                        'diagnostic_caution': 'This is an image-classification result, not a '
                                              'confirmed field diagnosis. Similar symptoms can '
                                              'have different causes; confirm with a qualified '
                                              'plant pathologist or local agricultural extension '
                                              'service before high-impact action. The prediction '
                                              'is not a confirmed field diagnosis; look-alike '
                                              'biotic and abiotic causes may require examination '
                                              'or laboratory testing.',
                        'management': ['Use healthy seedlings and inspect plants regularly for '
                                       'whiteflies.',
                                       'Remove severely symptomatic plants only in accordance with '
                                       'local extension guidance.',
                                       'Manage weeds and volunteer host plants and use '
                                       'insect-proof nursery netting.'],
                        'nutrient_guidance': None,
                        'prevention': ['Use disease-free planting material and protect nursery '
                                       'seedlings from vector entry.',
                                       'Monitor whitefly populations and avoid moving suspect '
                                       'seedlings between fields.'],
                        'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                        'sources': [{'organization': 'TNAU Agritech Portal',
                                     'title': 'Chilli viral diseases and leaf curl',
                                     'url': 'https://agritech.tnau.ac.in/crop_protection/chilli_diseases_7.html'}],
                        'spread': ['Chilli leaf-curl viruses are commonly transmitted by '
                                   'whiteflies; infected planting material and nearby host plants '
                                   'may contribute to disease spread.'],
                        'symptoms': ['Leaves may curl, crinkle, become smaller or distorted.',
                                     'Plants may show shortened internodes, stunting and reduced '
                                     'flowering.'],
                        'treatment_note': 'No chemical treatment is prescribed by this educational '
                                          'entry. Confirm the condition and consult current local '
                                          'agricultural-extension guidance and the applicable '
                                          'product label before considering any crop-protection '
                                          'product.',
                        'type': 'viral_disease'},
 'Chilli___Leaf_Spot': {'causal_agent': None,
                        'chemical_treatment': None,
                        'condition': 'Leaf Spot',
                        'crop': 'Chilli',
                        'diagnostic_caution': 'The model predicts a dataset label from an image; '
                                              'it does not confirm the pathogen, distinguish all '
                                              'look-alike conditions, or assess disease severity.',
                        'management': ['Inspect multiple leaves and the whole plant; seek local '
                                       'plant-pathology confirmation before choosing '
                                       'disease-specific control.',
                                       'Use clean planting material and avoid working among wet '
                                       'plants when a transmissible disease is suspected.',
                                       'Do not apply a fungicide or bactericide solely from this '
                                       'image prediction.'],
                        'nutrient_guidance': None,
                        'prevention': ['Use healthy, locally recommended planting material and '
                                       'resistant varieties where available.',
                                       'Monitor the crop regularly and follow crop-specific '
                                       'sanitation and rotation guidance.'],
                        'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                        'sources': [{'organization': 'Tamil Nadu Agricultural University (TNAU) '
                                                     'Agritech Portal',
                                     'title': 'Chilli Cercospora leaf spot: one documented cause '
                                              'and symptom pattern; generic model label is not '
                                              'species-specific',
                                     'url': 'https://agritech.tnau.ac.in/crop_protection/chilli_diseases_5.html'}],
                        'spread': ['Chilli can develop leaf spots from more than one cause. TNAU '
                                   'documents Cercospora capsici leaf spot, but this broad model '
                                   'label does not establish that pathogen or exclude bacterial '
                                   'and abiotic look-alikes.'],
                        'symptoms': ['Discrete spots may appear on leaves and can vary in colour, '
                                     'size, and margin; this broad class does not identify a '
                                     'specific pathogen.'],
                        'treatment_note': 'No chemical treatment is recommended here. Confirm the '
                                          'diagnosis and consult current crop-specific Indian '
                                          'label and registration guidance before any pesticide '
                                          'use.',
                        'type': 'disease_class_unverified'},
 'Chilli___Whitefly': {'causal_agent': 'Whitefly, Bemisia tabaci (identified in Kerala '
                                       'Agricultural University chilli guidance; species '
                                       'confirmation may require examination).',
                       'chemical_treatment': None,
                       'condition': 'Whitefly',
                       'crop': 'Chilli',
                       'diagnostic_caution': 'The model predicts a dataset label from an image; it '
                                             'does not confirm whitefly species, quantify '
                                             'infestation, or establish a virus infection.',
                       'management': ['Inspect the undersides of leaves for adults and immature '
                                      'stages and confirm the pest before taking action.',
                                      'Use integrated pest management, monitor populations and '
                                      'conserve natural enemies. Kerala Agricultural University '
                                      'describes clipping and destroying severely affected plant '
                                      'parts and use of yellow sticky traps.',
                                      'Do not apply an insecticide solely because of this image '
                                      'prediction; obtain crop- and location-specific advice.'],
                       'nutrient_guidance': None,
                       'prevention': ['Monitor chilli plants regularly, especially leaf '
                                      'undersides, and inspect seedlings before planting.',
                                      'Use locally recommended nursery protection and field '
                                      'sanitation practices; conserve beneficial insects where '
                                      'possible.'],
                       'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                       'sources': [{'organization': 'Kerala Agricultural University (KAU) Agri '
                                                    'Infotech Portal',
                                    'title': 'Chilli whitefly: Bemisia tabaci, damage symptoms and '
                                             'non-chemical management guidance',
                                    'url': 'https://celkau.in/crops/Vegetables/chilli/whitefly.php'},
                                   {'organization': 'Indian Journal of Plant Protection (ICAR '
                                                    'e-Pubs)',
                                    'title': 'Population dynamics of sucking pests including '
                                             'Bemisia tabaci in chilli pepper',
                                    'url': 'https://epubs.icar.org.in/index.php/IJPP/article/view/111887'}],
                       'spread': ['Adult whiteflies move between host plants and can transmit '
                                  'certain plant viruses, including begomoviruses associated with '
                                  'chilli leaf curl. A whitefly image classification does not '
                                  'establish that a plant is virus-infected.'],
                       'symptoms': ['Nymphs and adults feed on leaf sap, which can reduce plant '
                                    'vigour and contribute to yellowing and leaf drop. Whiteflies '
                                    'are small, pale insects usually found on leaf undersides; '
                                    'honeydew and sooty mould may occur with infestation.'],
                       'treatment_note': 'No chemical treatment or dosage is prescribed. Confirm '
                                         'the pest and consult current local '
                                         'agricultural-extension guidance and applicable Indian '
                                         'product-label requirements before considering any '
                                         'crop-protection product.',
                       'type': 'arthropod_pest'},
 'Chilli___healthy': {'causal_agent': None,
                      'chemical_treatment': None,
                      'condition': 'healthy',
                      'crop': 'Chilli',
                      'diagnostic_caution': 'A healthy prediction is a model classification, not a '
                                            'guarantee that the plant is disease-free.',
                      'management': ['Continue routine crop monitoring and follow locally '
                                     'recommended agronomic practices.',
                                     'If symptoms are visible despite this prediction, obtain a '
                                     'second assessment; the classifier can miss conditions.'],
                      'nutrient_guidance': None,
                      'prevention': ['Use clean planting material, maintain appropriate spacing '
                                     'and irrigation, and monitor plants regularly.'],
                      'review_status': 'REQUIRES_SOURCE_REVIEW',
                      'sources': [],
                      'spread': ['Not applicable to a healthy-class prediction.'],
                      'symptoms': ['The classifier assigned the healthy class. This is not a '
                                   'guarantee that the whole plant is free from disease, pests, or '
                                   'nutrient stress.'],
                      'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                        'prediction.',
                      'type': 'healthy'},
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {'causal_agent': 'Cercospora zeae-maydis '
                                                                        'and related Cercospora '
                                                                        'species',
                                                        'chemical_treatment': None,
                                                        'condition': 'Gray leaf spot',
                                                        'crop': 'Corn (maize)',
                                                        'diagnostic_caution': 'This is an '
                                                                              'image-classification '
                                                                              'result, not a '
                                                                              'confirmed field '
                                                                              'diagnosis. Similar '
                                                                              'symptoms can have '
                                                                              'different causes; '
                                                                              'confirm with a '
                                                                              'qualified plant '
                                                                              'pathologist or '
                                                                              'local agricultural '
                                                                              'extension service '
                                                                              'before high-impact '
                                                                              'action. The '
                                                                              'prediction is not a '
                                                                              'confirmed field '
                                                                              'diagnosis; '
                                                                              'look-alike biotic '
                                                                              'and abiotic causes '
                                                                              'may require '
                                                                              'examination or '
                                                                              'laboratory testing.',
                                                        'management': ['Scout lower leaves first '
                                                                       'and track whether lesions '
                                                                       'are moving upward toward '
                                                                       'the upper canopy.',
                                                                       'Manage infected maize '
                                                                       'residue according to local '
                                                                       'production practices '
                                                                       'because residue is an '
                                                                       'important source of '
                                                                       'primary inoculum.',
                                                                       'Avoid relying on a single '
                                                                       'management tactic; combine '
                                                                       'rotation, residue '
                                                                       'management and resistant '
                                                                       'or tolerant hybrids where '
                                                                       'appropriate.'],
                                                        'nutrient_guidance': None,
                                                        'prevention': ['Rotate maize with non-host '
                                                                       'crops where feasible to '
                                                                       'reduce the amount of '
                                                                       'infected maize residue '
                                                                       'carried into the next '
                                                                       'season.',
                                                                       'Choose hybrids with good '
                                                                       'gray-leaf-spot resistance '
                                                                       'when suitable for the '
                                                                       'region.',
                                                                       'Reduce prolonged leaf '
                                                                       'wetness and manage residue '
                                                                       'rather than leaving '
                                                                       'heavily infected maize '
                                                                       'debris as the main '
                                                                       'inoculum source.'],
                                                        'review_status': 'REQUIRES_SOURCE_REVIEW',
                                                        'sources': [{'organization': 'University '
                                                                                     'of Minnesota '
                                                                                     'Extension',
                                                                     'title': 'Gray leaf spot of '
                                                                              'corn',
                                                                     'url': 'https://extension.umn.edu/corn-pest-management/gray-leaf-spot-corn'}],
                                                        'spread': ['The fungus survives on '
                                                                   'infected maize residue and '
                                                                   'produces spores that infect '
                                                                   'new maize foliage.',
                                                                   'Spores are dispersed primarily '
                                                                   'by wind and rain splash during '
                                                                   'humid periods.',
                                                                   'Continuous maize production '
                                                                   'and abundant infected residue '
                                                                   'can increase the local '
                                                                   'inoculum source.'],
                                                        'symptoms': ['Rectangular gray to tan '
                                                                     'lesions develop on maize '
                                                                     'leaves, often becoming more '
                                                                     'obvious as they expand along '
                                                                     'the leaf veins.',
                                                                     'Older lesions can coalesce '
                                                                     'into large areas of dead '
                                                                     'leaf tissue.',
                                                                     'Severe infection reduces '
                                                                     'green leaf area during grain '
                                                                     'filling.'],
                                                        'treatment_note': 'Chemical decisions '
                                                                          'depend on hybrid '
                                                                          'susceptibility, disease '
                                                                          'pressure and crop '
                                                                          'stage; no chemical '
                                                                          'treatment is prescribed '
                                                                          'here.',
                                                        'type': 'Fungal Disease'},
 'Corn_(maize)___Common_rust_': {'causal_agent': 'Puccinia sorghi',
                                 'chemical_treatment': None,
                                 'condition': 'Common rust',
                                 'crop': 'Corn (maize)',
                                 'diagnostic_caution': 'The model predicts a dataset label from an '
                                                       'image; it does not confirm the pathogen, '
                                                       'distinguish all look-alike conditions, or '
                                                       'assess disease severity. Confirm uncertain '
                                                       'cases with a qualified plant-health '
                                                       'professional.',
                                 'management': ['Scout leaves for developing rust pustules, '
                                                'particularly during cool and humid periods.',
                                                'Use resistant or tolerant hybrids where available '
                                                'for the production region.',
                                                'Protect the upper green leaves during grain '
                                                'filling by combining resistance with timely '
                                                'disease monitoring.'],
                                 'nutrient_guidance': None,
                                 'prevention': ['Plant hybrids with resistance to the prevalent '
                                                'common-rust populations in the region.',
                                                'Avoid relying on susceptible hybrids where '
                                                'recurring rust pressure is known.',
                                                'Scout early so an increase in rust can be '
                                                'recognized before the upper canopy becomes '
                                                'heavily infected.'],
                                 'review_status': 'REQUIRES_SOURCE_REVIEW',
                                 'sources': [{'organization': 'University of Minnesota Extension',
                                              'title': 'Corn common rust',
                                              'url': 'https://extension.umn.edu/corn-pest-management/common-rust-corn'}],
                                 'spread': ['Airborne rust spores can travel long distances from '
                                            'infected maize or alternate hosts.',
                                            'New infections are favored by cool, humid conditions '
                                            'and extended periods of leaf wetness.',
                                            'The disease can spread rapidly through a crop when '
                                            'susceptible foliage remains favorable for infection.'],
                                 'symptoms': ['Small reddish-brown to cinnamon-colored rust '
                                              'pustules develop on maize leaves.',
                                              'Pustules occur on both leaf surfaces and release '
                                              'powdery spores when they rupture.',
                                              'Heavy infection can cause premature leaf senescence '
                                              'and reduce photosynthetic leaf area.'],
                                 'treatment_note': 'No chemical treatment is prescribed here; '
                                                   'management should follow local maize '
                                                   'disease-risk and crop-stage recommendations.',
                                 'type': 'Fungal Disease'},
 'Corn_(maize)___Maize_Lethal_Necrosis': {'causal_agent': 'Co-infection involving maize chlorotic '
                                                          'mottle virus and a potyvirus such as '
                                                          'Sugarcane mosaic virus',
                                          'chemical_treatment': None,
                                          'condition': 'Maize lethal necrosis',
                                          'crop': 'Corn (maize)',
                                          'diagnostic_caution': 'The classifier cannot detect or '
                                                                'distinguish the viruses '
                                                                'individually and cannot confirm '
                                                                'the required co-infection. '
                                                                'Laboratory or official '
                                                                'plant-health confirmation is '
                                                                'needed for suspected MLN. The '
                                                                'prediction is not a confirmed '
                                                                'field diagnosis; look-alike '
                                                                'biotic and abiotic causes may '
                                                                'require examination or laboratory '
                                                                'testing.',
                                          'management': ['Remove and destroy severely affected '
                                                         'plants where locally recommended to '
                                                         'reduce sources of virus.',
                                                         'Use tested, disease-free seed and avoid '
                                                         'carrying infected plant material between '
                                                         'fields.',
                                                         'Manage relevant insect vectors as part '
                                                         'of an integrated disease-control program '
                                                         'rather than attempting to cure infected '
                                                         'plants.'],
                                          'nutrient_guidance': None,
                                          'prevention': ['Use certified or tested seed and avoid '
                                                         'seed lots with known virus problems.',
                                                         'Monitor maize early for characteristic '
                                                         'mosaic, chlorosis and severe stunting.',
                                                         'Coordinate vector management and '
                                                         'sanitation because preventing '
                                                         'introduction and secondary spread is '
                                                         'more important than attempting to cure '
                                                         'infected plants.'],
                                          'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                                          'sources': [{'organization': 'CABI',
                                                       'title': 'Maize lethal necrosis disease',
                                                       'url': 'https://www.cabi.org/isc/datasheet/113284'},
                                                      {'organization': 'International Maize and '
                                                                       'Wheat Improvement Center '
                                                                       '(CIMMYT)',
                                                       'title': 'MLN Overview — causes and '
                                                                'transmission',
                                                       'url': 'https://mln.cimmyt.org/mln-overview/'},
                                                      {'organization': 'International Maize and '
                                                                       'Wheat Improvement Center '
                                                                       '(CIMMYT)',
                                                       'title': 'Causes & Transmission',
                                                       'url': 'https://mln.cimmyt.org/causes-symptoms/'}],
                                          'spread': ['Maize lethal necrosis results from '
                                                     'co-infection by maize chlorotic mottle virus '
                                                     '(MCMV) and a compatible potyvirus.',
                                                     'MCMV can be transmitted by thrips and '
                                                     'chrysomelid beetles; potyviruses such as '
                                                     'sugarcane mosaic virus are primarily '
                                                     'transmitted by aphids.',
                                                     'MCMV can also be associated with '
                                                     'contaminated seed, soil or plant debris and '
                                                     'mechanical transfer; the importance of these '
                                                     'routes varies by setting.'],
                                          'symptoms': ['Leaves develop mottling, chlorosis and '
                                                       'necrotic streaking that can progress from '
                                                       'lower leaves upward.',
                                                       'Plants may become severely stunted and '
                                                       'show premature drying of leaves.',
                                                       'In severe cases, plants fail to produce '
                                                       'normal ears or grain.'],
                                          'treatment_note': 'There is no curative antiviral '
                                                            'treatment prescribed here. Management '
                                                            'focuses on clean seed, vector '
                                                            'management, field sanitation and '
                                                            'prevention of virus introduction.',
                                          'type': 'Viral Disease'},
 'Corn_(maize)___Maize_Streak_Virus': {'causal_agent': 'Maize streak virus (MSV)',
                                       'chemical_treatment': None,
                                       'condition': 'Maize streak virus disease',
                                       'crop': 'Corn (maize)',
                                       'diagnostic_caution': 'The model predicts a dataset label '
                                                             'from an image; it does not confirm '
                                                             'the pathogen, distinguish all '
                                                             'look-alike conditions, or assess '
                                                             'disease severity.',
                                       'management': ['Scout young maize for characteristic linear '
                                                      'streaks and monitor vector activity where '
                                                      'local guidance recommends it.',
                                                      'Remove heavily infected volunteer maize and '
                                                      'manage grassy hosts around production areas '
                                                      'when practical.',
                                                      'Use locally recommended resistant or '
                                                      'tolerant maize varieties where available.'],
                                       'nutrient_guidance': None,
                                       'prevention': ['Use resistant or tolerant varieties suited '
                                                      'to the local maize-streak risk.',
                                                      'Control volunteer maize and important '
                                                      'grassy hosts around fields to reduce virus '
                                                      'and vector reservoirs.',
                                                      'Establish crops using clean seed and '
                                                      'monitor young plants early, when infection '
                                                      'has the greatest effect on crop '
                                                      'development.'],
                                       'review_status': 'REQUIRES_SOURCE_REVIEW',
                                       'sources': [{'organization': 'CABI',
                                                    'title': 'Maize streak virus',
                                                    'url': 'https://www.cabi.org/isc/datasheet/34731'}],
                                       'spread': ['Maize streak virus is transmitted primarily by '
                                                  'leafhopper vectors, especially Cicadulina '
                                                  'species.',
                                                  'Vector feeding transfers the virus from '
                                                  'infected plants to susceptible maize.',
                                                  'Volunteer maize and grassy hosts can help '
                                                  'maintain vector and virus sources between '
                                                  'crops.'],
                                       'symptoms': ['Narrow pale-green to yellow streaks develop '
                                                    'along leaf veins and can become numerous '
                                                    'across the leaf blade.',
                                                    'Young infected plants can become severely '
                                                    'stunted and may have shortened internodes.',
                                                    'Severe early infection can prevent normal ear '
                                                    'formation and substantially reduce yield.'],
                                       'treatment_note': 'There is no curative antiviral treatment '
                                                         'prescribed here; prevention depends on '
                                                         'resistant varieties, vector management '
                                                         'and reduction of virus reservoirs.',
                                       'type': 'Viral Disease'},
 'Corn_(maize)___Northern_Leaf_Blight': {'causal_agent': 'Exserohilum turcicum (syn. Setosphaeria '
                                                         'turcica)',
                                         'chemical_treatment': None,
                                         'condition': 'Maize northern leaf blight',
                                         'crop': 'Maize',
                                         'diagnostic_caution': 'The model predicts a dataset label '
                                                               'from an image; it does not confirm '
                                                               'the pathogen, distinguish all '
                                                               'look-alike conditions, or assess '
                                                               'disease severity. Confirm '
                                                               'uncertain cases with a qualified '
                                                               'plant-health professional.',
                                         'management': ['Inspect lower leaves and the full plant '
                                                        'for elongated cigar-shaped lesions; '
                                                        'obtain confirmation if symptoms are '
                                                        'unclear.',
                                                        'Manage infected maize residues and crop '
                                                        'rotation according to local '
                                                        'agricultural-extension recommendations.'],
                                         'nutrient_guidance': None,
                                         'prevention': ['Use locally recommended hybrids with '
                                                        'suitable resistance where available.',
                                                        'Monitor crops during cool, wet or humid '
                                                        'periods and avoid carrying infected crop '
                                                        'debris into new plantings.'],
                                         'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                                         'sources': [{'organization': 'Tamil Nadu Agricultural '
                                                                      'University (TNAU) Agritech '
                                                                      'Portal',
                                                      'title': 'Maize leaf blight: Exserohilum '
                                                               'turcicum and disease survival and '
                                                               'spread',
                                                      'url': 'https://agritech.tnau.ac.in/crop_protection/maize_disease_new/maize_2.html'}],
                                         'spread': ['The TNAU maize guide describes survival on '
                                                    'infected plant debris and spread by '
                                                    'wind-borne spores. Wet, humid and relatively '
                                                    'cool conditions favour disease development.'],
                                         'symptoms': ['Long, cigar-shaped grey-green to tan '
                                                      'lesions may develop on leaves, often '
                                                      'beginning on lower foliage. Lesions can '
                                                      'enlarge and coalesce, causing extensive '
                                                      'blighting.'],
                                         'treatment_note': 'No chemical treatment is prescribed by '
                                                           'this educational entry. Confirm the '
                                                           'diagnosis and consult current local '
                                                           'agricultural-extension guidance and '
                                                           'applicable Indian product-label '
                                                           'requirements before considering any '
                                                           'crop-protection product.',
                                         'type': 'fungal_disease'},
 'Corn_(maize)___healthy': {'causal_agent': None,
                            'chemical_treatment': None,
                            'condition': 'healthy',
                            'crop': 'Maize',
                            'diagnostic_caution': 'A healthy prediction is a model classification, '
                                                  'not a guarantee that the plant is disease-free.',
                            'management': ['Continue routine crop monitoring and follow locally '
                                           'recommended agronomic practices.',
                                           'If symptoms are visible despite this prediction, '
                                           'obtain a second assessment; the classifier can miss '
                                           'conditions.'],
                            'nutrient_guidance': None,
                            'prevention': ['Use clean planting material, maintain appropriate '
                                           'spacing and irrigation, and monitor plants regularly.'],
                            'review_status': 'REQUIRES_SOURCE_REVIEW',
                            'sources': [],
                            'spread': ['Not applicable to a healthy-class prediction.'],
                            'symptoms': ['The classifier assigned the healthy class. This is not a '
                                         'guarantee that the whole plant is free from disease, '
                                         'pests, or nutrient stress.'],
                            'treatment_note': 'No disease treatment is indicated by a '
                                              'healthy-class prediction.',
                            'type': 'healthy'},
 'Grape___Black_rot': {'causal_agent': 'Guignardia bidwellii',
                       'chemical_treatment': None,
                       'condition': 'Black rot',
                       'crop': 'Grape',
                       'diagnostic_caution': 'The model predicts a dataset label from an image; it '
                                             'does not confirm the pathogen, distinguish all '
                                             'look-alike conditions, or assess disease severity.',
                       'management': ['Remove and destroy mummified grape berries and infected '
                                      'cane material because these tissues can produce spores.',
                                      'Improve canopy airflow and reduce prolonged wetness around '
                                      'leaves and clusters.',
                                      'Scout during periods of wet weather and pay particular '
                                      'attention to developing fruit and nearby mummies.'],
                       'nutrient_guidance': None,
                       'prevention': ['Remove grape mummies from vines and vineyard floors before '
                                      "the next season's infection period.",
                                      'Prune and train vines to improve light penetration and '
                                      'airflow through the fruiting zone.',
                                      'Avoid leaving infected fruit and cane material in the '
                                      'canopy where it can produce spores during rain.'],
                       'review_status': 'REQUIRES_SOURCE_REVIEW',
                       'sources': [{'organization': 'UC IPM',
                                    'title': 'Grape Pest Management Guidelines',
                                    'url': 'https://ipm.ucanr.edu/agriculture/grape/'}],
                       'spread': ['The fungus survives in mummified berries and infected cane or '
                                  'leaf tissue left in the vineyard.',
                                  'Spores are released during wet periods and spread primarily by '
                                  'rain splash.',
                                  'New infections are favored by susceptible young tissue '
                                  'remaining wet for sufficient periods.'],
                       'symptoms': ['Small reddish-brown leaf spots can enlarge and develop dark '
                                    'margins.',
                                    'Young berries can develop light-colored spots that enlarge '
                                    'and turn dark, eventually becoming shriveled black mummified '
                                    'fruit.',
                                    'Black pycnidia can develop on mummified berries and infected '
                                    'tissues.'],
                       'treatment_note': 'The most disease-specific management target is removal '
                                         'of overwintering mummified fruit and infected tissues; '
                                         'no chemical treatment is prescribed here.',
                       'type': 'Fungal Disease'},
 'Grape___Esca_(Black_Measles)': {'causal_agent': 'Complex of trunk-disease fungi including '
                                                  'Phaeoacremonium aleophilum and Phaeomoniella '
                                                  'chlamydospora',
                                  'chemical_treatment': None,
                                  'condition': 'Esca (Black Measles)',
                                  'crop': 'Grape',
                                  'diagnostic_caution': 'The model predicts a dataset label from '
                                                        'an image; it does not confirm the '
                                                        'pathogen, distinguish all look-alike '
                                                        'conditions, or assess disease severity.',
                                  'management': ['Identify and flag vines showing trunk-disease '
                                                 'symptoms so affected wood can be managed '
                                                 'separately.',
                                                 'Carry out sanitation and vine surgery before '
                                                 'major rain periods, removing infected woody '
                                                 'material where recommended.',
                                                 'Minimize unnecessary pruning wounds and protect '
                                                 'pruning operations from spreading contaminated '
                                                 'material between vines.'],
                                  'nutrient_guidance': None,
                                  'prevention': ['Sanitize pruning tools and avoid transferring '
                                                 'infected wood between vines.',
                                                 'Schedule major pruning and sanitation work with '
                                                 'local disease-risk periods in mind, particularly '
                                                 'before wet weather.',
                                                 'Inspect older vines for recurring foliar '
                                                 'striping, fruit symptoms and trunk discoloration '
                                                 'so suspect vines can be investigated early.'],
                                  'review_status': 'REQUIRES_SOURCE_REVIEW',
                                  'sources': [{'organization': 'UC IPM',
                                               'title': 'Esca (Black Measles)',
                                               'url': 'https://ipm.ucanr.edu/agriculture/grape/esca-black-measles/'}],
                                  'spread': ['Disease-causing fungi persist in infected woody '
                                             'tissues and produce spores from overwintering '
                                             'structures.',
                                             'Rain during fall through spring can release spores '
                                             'that infect fresh pruning wounds.',
                                             'Once established in woody tissue, the infection can '
                                             'become permanent and localized within the vine.'],
                                  'symptoms': ['Leaves can develop interveinal striping that '
                                               'becomes necrotic and may cause premature leaf '
                                               'drying and drop.',
                                               'Berries can develop small dark spots bordered by '
                                               'brown-purple rings and may crack or dry in severe '
                                               'cases.',
                                               'Cross-sections of affected trunks, cordons, canes '
                                               'or spurs can show dark concentric discoloration.'],
                                  'treatment_note': 'Esca is a trunk disease complex and '
                                                    'established wood infections cannot be '
                                                    'reliably eradicated by foliar fungicide '
                                                    'treatment. This knowledge base therefore does '
                                                    'not prescribe a chemical treatment.',
                                  'type': 'Fungal Disease'},
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {'causal_agent': 'Pseudocercospora vitis (synonyms '
                                                                'used in older literature include '
                                                                'Isariopsis clavispora)',
                                                'chemical_treatment': None,
                                                'condition': 'Isariopsis leaf spot / leaf blight',
                                                'crop': 'Grape',
                                                'diagnostic_caution': 'The model predicts a '
                                                                      'dataset label from an '
                                                                      'image; it does not confirm '
                                                                      'the pathogen, distinguish '
                                                                      'all look-alike conditions, '
                                                                      'or assess disease severity.',
                                                'management': ['Remove severely diseased fallen or '
                                                               'attached leaf material where '
                                                               'practical to reduce local '
                                                               'inoculum.',
                                                               'Improve canopy ventilation through '
                                                               'appropriate training and pruning '
                                                               'so leaves dry faster.',
                                                               'Scout lower and older leaves for '
                                                               'expanding lesions and track '
                                                               'whether symptoms are moving into '
                                                               'the fruiting canopy.'],
                                                'nutrient_guidance': None,
                                                'prevention': ['Maintain an open, well-trained '
                                                               'grape canopy with good air '
                                                               'movement through the leaf zone.',
                                                               'Avoid prolonged leaf wetness from '
                                                               'irrigation practices where '
                                                               'feasible.',
                                                               'Remove heavily diseased leaf '
                                                               'debris and maintain vineyard '
                                                               'sanitation between seasons.'],
                                                'review_status': 'REQUIRES_SOURCE_REVIEW',
                                                'sources': [{'organization': 'TNAU Agritech Portal',
                                                             'title': 'Grape disease management '
                                                                      'resources',
                                                             'url': 'https://agritech.tnau.ac.in/crop_protection/grapes_diseases_2.html'}],
                                                'spread': ['Fungal spores produced on infected '
                                                           'leaf tissue can spread to healthy '
                                                           'foliage during humid or wet weather.',
                                                           'Rain splash and movement of infected '
                                                           'leaf material can contribute to local '
                                                           'spread.',
                                                           'Dense canopies that remain humid for '
                                                           'long periods favor leaf-spot '
                                                           'development.'],
                                                'symptoms': ['Brown to reddish-brown leaf spots '
                                                             'can enlarge and merge into irregular '
                                                             'blighted areas.',
                                                             'Older leaves may show extensive '
                                                             'necrosis when infection is severe.',
                                                             'Severe defoliation can reduce the '
                                                             'functional leaf area available for '
                                                             'fruit development and ripening.'],
                                                'treatment_note': 'No chemical treatment is '
                                                                  'prescribed here; management '
                                                                  'emphasizes sanitation, canopy '
                                                                  'airflow and monitoring.',
                                                'type': 'Fungal Disease'},
 'Grape___healthy': {'causal_agent': None,
                     'chemical_treatment': None,
                     'condition': 'healthy',
                     'crop': 'Grape',
                     'diagnostic_caution': 'A healthy prediction is a model classification, not a '
                                           'guarantee that the plant is disease-free.',
                     'management': ['Continue routine crop monitoring and follow locally '
                                    'recommended agronomic practices.',
                                    'If symptoms are visible despite this prediction, obtain a '
                                    'second assessment; the classifier can miss conditions.'],
                     'nutrient_guidance': None,
                     'prevention': ['Use clean planting material, maintain appropriate spacing and '
                                    'irrigation, and monitor plants regularly.'],
                     'review_status': 'REQUIRES_SOURCE_REVIEW',
                     'sources': [],
                     'spread': ['Not applicable to a healthy-class prediction.'],
                     'symptoms': ['The classifier assigned the healthy class. This is not a '
                                  'guarantee that the whole plant is free from disease, pests, or '
                                  'nutrient stress.'],
                     'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                       'prediction.',
                     'type': 'healthy'},
 'Groundnut___Early_Leaf_Spot': {'causal_agent': 'Cercospora arachidicola (also reported as '
                                                 'Mycosphaerella arachidis)',
                                 'chemical_treatment': None,
                                 'condition': 'Groundnut early leaf spot',
                                 'crop': 'Groundnut',
                                 'diagnostic_caution': 'This is an image-classification result, '
                                                       'not a confirmed field diagnosis. Similar '
                                                       'symptoms can have different causes; '
                                                       'confirm with a qualified plant pathologist '
                                                       'or local agricultural extension service '
                                                       'before high-impact action. The prediction '
                                                       'is not a confirmed field diagnosis; '
                                                       'look-alike biotic and abiotic causes may '
                                                       'require examination or laboratory testing.',
                                 'management': ['Remove or bury infected crop residues and '
                                                'volunteer groundnut plants where practical.',
                                                'Use locally recommended tolerant varieties and '
                                                'rotate with non-host crops, preferably cereals.',
                                                'Avoid unnecessary overhead irrigation and monitor '
                                                'lower leaves for early symptoms.'],
                                 'nutrient_guidance': None,
                                 'prevention': ['Use clean seed and maintain field sanitation.',
                                                'Follow locally recommended crop rotation and '
                                                'variety guidance.'],
                                 'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                                 'sources': [{'organization': 'TNAU Agritech Portal',
                                              'title': 'Groundnut early leaf spot: symptoms, '
                                                       'pathogen and management',
                                              'url': 'https://agritech.tnau.ac.in/agriculture/Crop-production-pathology-crp-4.html'},
                                             {'organization': 'TNAU Agritech Portal',
                                              'title': 'Organic management of groundnut diseases',
                                              'url': 'https://agritech.tnau.ac.in/org_farm/orgfarm_agridiseases.html'}],
                                 'spread': ['The pathogen can persist in crop debris; primary and '
                                            'secondary spores spread through air, with infection '
                                            'favoured by prolonged leaf wetness and high '
                                            'humidity.'],
                                 'symptoms': ['Small brown to reddish-brown circular lesions may '
                                              'develop on leaflets, often with a conspicuous '
                                              'yellow halo.',
                                              'Lesions may also occur on petioles, stems and '
                                              'stipules.'],
                                 'treatment_note': 'No chemical treatment is prescribed by this '
                                                   'educational entry. Confirm the condition and '
                                                   'consult current local agricultural-extension '
                                                   'guidance and the applicable product label '
                                                   'before considering any crop-protection '
                                                   'product.',
                                 'type': 'fungal_disease'},
 'Groundnut___Early_Rust': {'causal_agent': 'Puccinia arachidis',
                            'chemical_treatment': None,
                            'condition': 'Groundnut rust (dataset label: Early Rust)',
                            'crop': 'Groundnut',
                            'diagnostic_caution': 'This is an image-classification result, not a '
                                                  'confirmed field diagnosis. Similar symptoms can '
                                                  'have different causes; confirm with a qualified '
                                                  'plant pathologist or local agricultural '
                                                  'extension service before high-impact action. '
                                                  'The prediction is not a confirmed field '
                                                  'diagnosis; look-alike biotic and abiotic causes '
                                                  'may require examination or laboratory testing.',
                            'management': ['Remove volunteer groundnut plants and manage infected '
                                           'crop debris.',
                                           'Use locally adapted tolerant varieties and crop '
                                           'rotation.',
                                           'Confirm the field condition with an agricultural '
                                           'extension worker if symptoms are atypical.'],
                            'nutrient_guidance': None,
                            'prevention': ['Maintain field sanitation and monitor leaves '
                                           'regularly.'],
                            'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                            'sources': [{'organization': 'TNAU Agritech Portal',
                                         'title': 'Groundnut rust: Puccinia arachidis, symptoms '
                                                  'and management',
                                         'url': 'https://agritech.tnau.ac.in/crop_protection/groundnut_diseases/groundnut_d3.html'}],
                            'spread': ['Rust spores are wind-dispersed; volunteer groundnut and '
                                       'infected crop debris can contribute to carryover.'],
                            'symptoms': ['Orange to reddish-brown powdery pustules may appear on '
                                         'leaf surfaces, often first on the lower surface.',
                                         'Severe infection may cause leaf tissue to become '
                                         'necrotic and dry.'],
                            'treatment_note': 'No chemical treatment is prescribed by this '
                                              'educational entry. Confirm the condition and '
                                              'consult current local agricultural-extension '
                                              'guidance and the applicable product label before '
                                              'considering any crop-protection product.',
                            'type': 'fungal_disease'},
 'Groundnut___Late_Leaf_Spot': {'causal_agent': 'Nothopassalora personata (older literature: '
                                                'Cercospora personata / Phaeoisariopsis personata)',
                                'chemical_treatment': None,
                                'condition': 'Groundnut late leaf spot',
                                'crop': 'Groundnut',
                                'diagnostic_caution': 'This is an image-classification result, not '
                                                      'a confirmed field diagnosis. Similar '
                                                      'symptoms can have different causes; confirm '
                                                      'with a qualified plant pathologist or local '
                                                      'agricultural extension service before '
                                                      'high-impact action. The prediction is not a '
                                                      'confirmed field diagnosis; look-alike '
                                                      'biotic and abiotic causes may require '
                                                      'examination or laboratory testing.',
                                'management': ['Remove volunteer groundnut plants and manage '
                                               'infected crop residues.',
                                               'Rotate with non-host crops, preferably cereals, '
                                               'and use locally recommended tolerant varieties.',
                                               'Monitor the crop during humid periods and seek '
                                               'local plant-pathology advice if defoliation '
                                               'progresses.'],
                                'nutrient_guidance': None,
                                'prevention': ['Use healthy seed and field sanitation.',
                                               'Avoid continuous groundnut cropping where disease '
                                               'pressure is high.'],
                                'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                                'sources': [{'organization': 'TNAU Agritech Portal',
                                             'title': 'Groundnut late leaf spot: symptoms, '
                                                      'pathogen and management',
                                             'url': 'https://agritech.tnau.ac.in/agriculture/Crop-production-pathology-crp-5.html'},
                                            {'organization': 'TNAU Agritech Portal',
                                             'title': 'Groundnut rust and late leaf spot advisory',
                                             'url': 'https://agritech.tnau.ac.in/govt_schemes_services/aas/groundnut_ex1.html'}],
                                'spread': ['The pathogen can persist in infected plant debris and '
                                           'may be carried by infected seed; spores spread through '
                                           'air and rain splash.'],
                                'symptoms': ['Dark brown to black, nearly circular lesions '
                                             'commonly develop on the lower surface of leaflets.',
                                             'Severe infection can cause lesions to merge, '
                                             'followed by premature leaf ageing and leaflet '
                                             'shedding.'],
                                'treatment_note': 'No chemical treatment is prescribed by this '
                                                  'educational entry. Confirm the condition and '
                                                  'consult current local agricultural-extension '
                                                  'guidance and the applicable product label '
                                                  'before considering any crop-protection product.',
                                'type': 'fungal_disease'},
 'Groundnut___Nutrition_Deficiency': {'causal_agent': None,
                                      'chemical_treatment': None,
                                      'condition': 'Groundnut nutrient-deficiency-like symptoms',
                                      'crop': 'Groundnut',
                                      'diagnostic_caution': 'Different nutrient deficiencies, root '
                                                            'problems, water stress, and diseases '
                                                            'can produce similar visual symptoms. '
                                                            'The prediction is not a confirmed '
                                                            'field diagnosis; look-alike biotic '
                                                            'and abiotic causes may require '
                                                            'examination or laboratory testing.',
                                      'management': ['Use soil testing and, where appropriate, '
                                                     'plant-tissue testing before applying a '
                                                     'nutrient correction.',
                                                     'Check soil pH, drainage, irrigation and root '
                                                     'health.',
                                                     'Follow locally recommended nutrient '
                                                     'correction based on test results.'],
                                      'nutrient_guidance': 'Soil or tissue testing is required to '
                                                           'identify the nutrient involved.',
                                      'prevention': ['Use soil-test-based fertilisation and '
                                                     'maintain balanced soil management.'],
                                      'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                                      'sources': [{'organization': 'Tamil Nadu Agricultural '
                                                                   'University (TNAU) Agritech '
                                                                   'Portal',
                                                   'title': 'Groundnut nutritional disorders: '
                                                            'zinc, iron and boron deficiency '
                                                            'context; confirm with soil/plant '
                                                            'testing',
                                                   'url': 'https://agritech.tnau.ac.in/org_farm/orgfarm_prac_agri_groundnut_diseases.html'}],
                                      'spread': ['Not infectious. Similar symptoms may result from '
                                                 'nutrient availability, soil pH, waterlogging, '
                                                 'drought or root damage.'],
                                      'symptoms': ['Chlorosis, interveinal yellowing, marginal '
                                                   'scorch, stunting or poor growth may occur.',
                                                   'The visible pattern depends on the nutrient, '
                                                   'soil pH, moisture, root health and other '
                                                   'stresses; the image label cannot identify a '
                                                   'specific deficient element.'],
                                      'treatment_note': 'Do not select a fertiliser from leaf '
                                                        'appearance alone; confirm the nutrient '
                                                        'issue through soil or plant-tissue '
                                                        'testing.',
                                      'type': 'abiotic_or_nutritional'},
 'Groundnut___Rust': {'causal_agent': 'Puccinia arachidis',
                      'chemical_treatment': None,
                      'condition': 'Groundnut rust',
                      'crop': 'Groundnut',
                      'diagnostic_caution': 'This is an image-classification result, not a '
                                            'confirmed field diagnosis. Similar symptoms can have '
                                            'different causes; confirm with a qualified plant '
                                            'pathologist or local agricultural extension service '
                                            'before high-impact action. The prediction is not a '
                                            'confirmed field diagnosis; look-alike biotic and '
                                            'abiotic causes may require examination or laboratory '
                                            'testing.',
                      'management': ['Remove volunteer groundnut plants and manage infected crop '
                                     'debris.',
                                     'Use locally adapted tolerant varieties and rotate crops '
                                     'where practical.',
                                     'Monitor both leaf surfaces and seek local extension advice '
                                     'if infection becomes severe.'],
                      'nutrient_guidance': None,
                      'prevention': ['Maintain field sanitation and use healthy planting material.',
                                     'Follow locally recommended sowing dates and crop-rotation '
                                     'practices.'],
                      'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                      'sources': [{'organization': 'TNAU Agritech Portal',
                                   'title': 'Groundnut rust: Puccinia arachidis, symptoms and '
                                            'management',
                                   'url': 'https://agritech.tnau.ac.in/crop_protection/groundnut_diseases/groundnut_d3.html'},
                                  {'organization': 'TNAU Agritech Portal',
                                   'title': 'Groundnut rust and late leaf spot advisory',
                                   'url': 'https://agritech.tnau.ac.in/govt_schemes_services/aas/groundnut_ex1.html'}],
                      'spread': ['Rust spores spread through air currents; volunteer groundnut '
                                 'plants and infected crop residues can contribute to disease '
                                 'carryover.'],
                      'symptoms': ['Orange to reddish-brown powdery pustules commonly appear first '
                                   'on the lower leaf surface and may also occur on the upper '
                                   'surface.',
                                   'Severe infection can cause leaves to become necrotic and dry '
                                   'while remaining attached to the plant.'],
                      'treatment_note': 'No chemical treatment is prescribed by this educational '
                                        'entry. Confirm the condition and consult current local '
                                        'agricultural-extension guidance and the applicable '
                                        'product label before considering any crop-protection '
                                        'product.',
                      'type': 'fungal_disease'},
 'Groundnut___healthy': {'causal_agent': None,
                         'chemical_treatment': None,
                         'condition': 'healthy',
                         'crop': 'Groundnut',
                         'diagnostic_caution': 'A healthy prediction is a model classification, '
                                               'not a guarantee that the plant is disease-free.',
                         'management': ['Continue routine crop monitoring and follow locally '
                                        'recommended agronomic practices.',
                                        'If symptoms are visible despite this prediction, obtain a '
                                        'second assessment; the classifier can miss conditions.'],
                         'nutrient_guidance': None,
                         'prevention': ['Use clean planting material, maintain appropriate spacing '
                                        'and irrigation, and monitor plants regularly.'],
                         'review_status': 'REQUIRES_SOURCE_REVIEW',
                         'sources': [],
                         'spread': ['Not applicable to a healthy-class prediction.'],
                         'symptoms': ['The classifier assigned the healthy class. This is not a '
                                      'guarantee that the whole plant is free from disease, pests, '
                                      'or nutrient stress.'],
                         'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                           'prediction.',
                         'type': 'healthy'},
 'Orange___Haunglongbing_(Citrus_greening)': {'causal_agent': 'Candidatus Liberibacter asiaticus '
                                                              '(citrus greening bacterium)',
                                              'chemical_treatment': None,
                                              'condition': 'Huanglongbing (citrus greening)',
                                              'crop': 'Orange',
                                              'diagnostic_caution': 'The model predicts a dataset '
                                                                    'label from an image; it does '
                                                                    'not confirm the pathogen, '
                                                                    'distinguish all look-alike '
                                                                    'conditions, or assess disease '
                                                                    'severity.',
                                              'management': ['Confirm suspect trees using an '
                                                             'appropriate diagnostic test because '
                                                             'HLB symptoms can resemble nutrient '
                                                             'deficiency and other disorders.',
                                                             'Use clean, pathogen-free propagation '
                                                             'material for new plantings.',
                                                             'Manage citrus psyllid populations as '
                                                             'part of an integrated program and '
                                                             'remove or manage confirmed infected '
                                                             'trees according to local regulatory '
                                                             'and extension guidance.'],
                                              'nutrient_guidance': None,
                                              'prevention': ['Establish orchards only with '
                                                             'certified or pathogen-tested '
                                                             'planting material.',
                                                             'Monitor new flushes for Asian citrus '
                                                             'psyllid activity because young flush '
                                                             'is an important feeding and '
                                                             'transmission stage.',
                                                             'Coordinate vector monitoring, clean '
                                                             'propagation material and removal of '
                                                             'confirmed infected sources rather '
                                                             'than treating HLB as a simple foliar '
                                                             'deficiency.'],
                                              'review_status': 'REQUIRES_SOURCE_REVIEW',
                                              'sources': [{'organization': 'TNAU Agritech Portal',
                                                           'title': 'Citrus Greening',
                                                           'url': 'https://agritech.tnau.ac.in/crop_protection/citrus_diseases_5.html'},
                                                          {'organization': 'TNAU Agritech Portal',
                                                           'title': 'Citrus Psyllid',
                                                           'url': 'https://agritech.tnau.ac.in/crop_protection/citrus_pest/citrus_3.html'}],
                                              'spread': ['The pathogen is transmitted by infected '
                                                         'budwood and by the Asian citrus psyllid, '
                                                         'Diaphorina citri.',
                                                         'Psyllids acquire the pathogen while '
                                                         'feeding on infected citrus and can '
                                                         'transmit it during subsequent feeding.',
                                                         'Movement of infected propagation '
                                                         'material can introduce HLB into new '
                                                         'orchards.'],
                                              'symptoms': ['Leaves show blotchy, asymmetric '
                                                           'mottling that can resemble nutrient '
                                                           'deficiency but does not follow a '
                                                           'simple uniform deficiency pattern.',
                                                           'Shoots may become upright with sparse '
                                                           'foliage and progressive twig dieback.',
                                                           'Fruit can remain partly green, become '
                                                           'small or lopsided, and have poor juice '
                                                           'and seed development.'],
                                              'treatment_note': 'HLB is a systemic disease with no '
                                                                'established curative treatment in '
                                                                'this knowledge base. Antibiotic '
                                                                'or pesticide use should not be '
                                                                'inferred from the image '
                                                                'prediction; confirmed diagnosis '
                                                                'and local regulatory guidance are '
                                                                'required.',
                                              'type': 'Bacterial Disease'},
 'Peach___Bacterial_spot': {'causal_agent': 'Xanthomonas arboricola pv. pruni',
                            'chemical_treatment': None,
                            'condition': 'Peach bacterial spot',
                            'crop': 'Peach',
                            'diagnostic_caution': 'The model predicts a dataset label from an '
                                                  'image; it does not confirm the pathogen, '
                                                  'distinguish all look-alike conditions, or '
                                                  'assess disease severity.',
                            'management': ['Remove heavily diseased plant material where practical '
                                           'and avoid working wet foliage when bacterial spread is '
                                           'likely.',
                                           'Improve canopy airflow so leaves and fruit dry rapidly '
                                           'after rain.',
                                           'Monitor young leaves and fruit during warm, wet '
                                           'periods because early infections can lead to repeated '
                                           'disease cycles.'],
                            'nutrient_guidance': None,
                            'prevention': ['Use disease-free nursery stock and avoid introducing '
                                           'infected planting material.',
                                           'Use irrigation practices that minimize prolonged '
                                           'wetting of peach foliage.',
                                           'Maintain an open canopy through appropriate pruning so '
                                           'leaves and fruit dry more quickly after rainfall.'],
                            'review_status': 'REQUIRES_SOURCE_REVIEW',
                            'sources': [{'organization': 'TNAU Agritech Portal',
                                         'title': 'Peach crop protection',
                                         'url': 'https://agritech.tnau.ac.in/crop_protection/crop_prot_insect_tem_peach_pest%26disease.html'}],
                            'spread': ['The bacterium can survive in infected plant tissues and '
                                       'can be moved by rain, irrigation splash and contact with '
                                       'contaminated material.',
                                       'Warm, wet conditions favor infection and repeated '
                                       'secondary spread.',
                                       'Pruning wounds and other openings can increase '
                                       'opportunities for bacterial entry.'],
                            'symptoms': ['Small water-soaked to dark lesions develop on young '
                                         'leaves and can enlarge into angular or irregular spots.',
                                         'Severe leaf infection can cause yellowing and premature '
                                         'leaf drop.',
                                         'Fruit may develop small dark, sunken or cracked lesions, '
                                         'especially where infection occurs on susceptible young '
                                         'fruit.'],
                            'treatment_note': 'Management should be based on local peach '
                                              'bacterial-spot guidance and disease pressure; no '
                                              'chemical treatment is prescribed here.',
                            'type': 'Bacterial Disease'},
 'Peach___healthy': {'causal_agent': None,
                     'chemical_treatment': None,
                     'condition': 'healthy',
                     'crop': 'Peach',
                     'diagnostic_caution': 'A healthy prediction is a model classification, not a '
                                           'guarantee that the plant is disease-free.',
                     'management': ['Continue routine crop monitoring and follow locally '
                                    'recommended agronomic practices.',
                                    'If symptoms are visible despite this prediction, obtain a '
                                    'second assessment; the classifier can miss conditions.'],
                     'nutrient_guidance': None,
                     'prevention': ['Use clean planting material, maintain appropriate spacing and '
                                    'irrigation, and monitor plants regularly.'],
                     'review_status': 'REQUIRES_SOURCE_REVIEW',
                     'sources': [],
                     'spread': ['Not applicable to a healthy-class prediction.'],
                     'symptoms': ['The classifier assigned the healthy class. This is not a '
                                  'guarantee that the whole plant is free from disease, pests, or '
                                  'nutrient stress.'],
                     'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                       'prediction.',
                     'type': 'healthy'},
 'Pepper,_bell___Bacterial_spot': {'causal_agent': 'Xanthomonas campestris pv. vesicatoria complex',
                                   'chemical_treatment': None,
                                   'condition': 'Bacterial spot',
                                   'crop': 'Bell pepper',
                                   'diagnostic_caution': 'The model predicts a dataset label from '
                                                         'an image; it does not confirm the '
                                                         'pathogen, distinguish all look-alike '
                                                         'conditions, or assess disease severity.',
                                   'management': ['Start with pathogen-negative or properly '
                                                  'treated seed and disease-free transplants.',
                                                  'Use drip or furrow irrigation rather than '
                                                  'overhead irrigation where feasible to reduce '
                                                  'splash spread.',
                                                  'Remove severely affected plant material and '
                                                  'avoid working through wet plants when bacterial '
                                                  'transfer is likely.'],
                                   'nutrient_guidance': None,
                                   'prevention': ['Use tested pathogen-negative seed and clean '
                                                  'transplants because seedborne introduction can '
                                                  'establish the disease in a field.',
                                                  'Rotate away from peppers for at least one '
                                                  'season where bacterial spot has been a '
                                                  'recurring problem.',
                                                  'Reduce leaf wetness and splash by using '
                                                  'appropriate irrigation and maintaining good '
                                                  'airflow around plants.'],
                                   'review_status': 'REQUIRES_SOURCE_REVIEW',
                                   'sources': [{'organization': 'UC IPM',
                                                'title': 'Bacterial Spot — Peppers',
                                                'url': 'https://ipm.ucanr.edu/agriculture/peppers/bacterial-spot/'}],
                                   'spread': ['The pathogen can be seedborne and can enter '
                                              'production through contaminated seed or infected '
                                              'transplants.',
                                              'Rain, sprinkler irrigation and other free water can '
                                              'disseminate bacteria from infected tissue to '
                                              'healthy tissue.',
                                              'High humidity and prolonged free moisture on plant '
                                              'surfaces favor disease development.'],
                                   'symptoms': ['Small angular, water-soaked leaf spots develop '
                                                'first, often on lower leaf surfaces, and later '
                                                'turn brown.',
                                                'Elongated raised lesions can occur on stems.',
                                                'Fruit lesions are circular, brown and raised, '
                                                'with a cracked or rough, wart-like surface.'],
                                   'treatment_note': 'No chemical treatment is prescribed here. '
                                                     'Copper products are used in some production '
                                                     'systems, but effectiveness and resistance '
                                                     'vary; any chemical decision should follow '
                                                     'current local label and extension guidance.',
                                   'type': 'Bacterial Disease'},
 'Pepper,_bell___healthy': {'causal_agent': None,
                            'chemical_treatment': None,
                            'condition': 'healthy',
                            'crop': 'Bell pepper',
                            'diagnostic_caution': 'A healthy prediction is a model classification, '
                                                  'not a guarantee that the plant is disease-free.',
                            'management': ['Continue routine crop monitoring and follow locally '
                                           'recommended agronomic practices.',
                                           'If symptoms are visible despite this prediction, '
                                           'obtain a second assessment; the classifier can miss '
                                           'conditions.'],
                            'nutrient_guidance': None,
                            'prevention': ['Use clean planting material, maintain appropriate '
                                           'spacing and irrigation, and monitor plants regularly.'],
                            'review_status': 'REQUIRES_SOURCE_REVIEW',
                            'sources': [],
                            'spread': ['Not applicable to a healthy-class prediction.'],
                            'symptoms': ['The classifier assigned the healthy class. This is not a '
                                         'guarantee that the whole plant is free from disease, '
                                         'pests, or nutrient stress.'],
                            'treatment_note': 'No disease treatment is indicated by a '
                                              'healthy-class prediction.',
                            'type': 'healthy'},
 'Potato___Early_blight': {'causal_agent': 'Alternaria solani',
                           'chemical_treatment': None,
                           'condition': 'Early blight',
                           'crop': 'Potato',
                           'diagnostic_caution': 'The model predicts a dataset label from an '
                                                 'image; it does not confirm the pathogen, '
                                                 'distinguish all look-alike conditions, or assess '
                                                 'disease severity.',
                           'management': ['Inspect more than one plant and compare symptoms with '
                                          'crop-specific guidance from a recognised '
                                          'agricultural-extension service.',
                                          'Remove or isolate affected material only when '
                                          'recommended for the confirmed condition; avoid moving '
                                          'potentially infected planting material.',
                                          'Improve general crop hygiene and avoid unnecessary '
                                          'handling of wet foliage.'],
                           'nutrient_guidance': None,
                           'prevention': ['Use healthy, locally recommended planting material and '
                                          'resistant varieties where available.',
                                          'Monitor the crop regularly and follow crop-specific '
                                          'sanitation and rotation guidance.'],
                           'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                           'sources': [{'organization': 'Tamil Nadu Agricultural University (TNAU) '
                                                        'Agritech Portal',
                                        'title': 'Potato early blight: Alternaria solani, symptoms '
                                                 'and survival/spread',
                                        'url': 'https://agritech.tnau.ac.in/crop_protection/crop_prot_crop%20diseases_veg_potato_2.html'}],
                           'spread': ['The pathogen can persist in infected plant debris and soil; '
                                      'spores can spread by wind and may move to nearby plants '
                                      'through rain or insects.'],
                           'symptoms': ['Brown to black necrotic leaf spots may develop, often '
                                        'with concentric rings; multiple lesions can merge and '
                                        'blight leaves.'],
                           'treatment_note': 'No chemical treatment is recommended here. Confirm '
                                             'the diagnosis and consult current crop-specific '
                                             'Indian label and registration guidance before any '
                                             'pesticide use.',
                           'type': 'fungal_disease'},
 'Potato___Late_blight': {'causal_agent': 'Phytophthora infestans',
                          'chemical_treatment': None,
                          'condition': 'Late blight',
                          'crop': 'Potato',
                          'diagnostic_caution': 'The model predicts a dataset label from an image; '
                                                'it does not confirm the pathogen, distinguish all '
                                                'look-alike conditions, or assess disease '
                                                'severity.',
                          'management': ['Inspect more than one plant and compare symptoms with '
                                         'crop-specific guidance from a recognised '
                                         'agricultural-extension service.',
                                         'Remove or isolate affected material only when '
                                         'recommended for the confirmed condition; avoid moving '
                                         'potentially infected planting material.',
                                         'Improve general crop hygiene and avoid unnecessary '
                                         'handling of wet foliage.'],
                          'nutrient_guidance': None,
                          'prevention': ['Use healthy, locally recommended planting material and '
                                         'resistant varieties where available.',
                                         'Monitor the crop regularly and follow crop-specific '
                                         'sanitation and rotation guidance.'],
                          'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                          'sources': [{'organization': 'Tamil Nadu Agricultural University (TNAU) '
                                                       'Agritech Portal',
                                       'title': 'Potato late blight: Phytophthora infestans, '
                                                'symptoms and spread',
                                       'url': 'https://agritech.tnau.ac.in/crop_protection/potato_phdiseases_4.html'}],
                          'spread': ['Infected tubers and soil can provide primary inoculum; '
                                     'airborne sporangia contribute to spread. Cool, humid and wet '
                                     'conditions favour disease development.'],
                          'symptoms': ['Water-soaked leaf lesions can turn purple-brown to black; '
                                       'white sporulation may appear on leaf undersides in humid '
                                       'conditions. Stems and tubers can also be affected.'],
                          'treatment_note': 'No chemical treatment is recommended here. Confirm '
                                            'the diagnosis and consult current crop-specific '
                                            'Indian label and registration guidance before any '
                                            'pesticide use.',
                          'type': 'oomycete_or_downy_mildew'},
 'Potato___healthy': {'causal_agent': None,
                      'chemical_treatment': None,
                      'condition': 'healthy',
                      'crop': 'Potato',
                      'diagnostic_caution': 'A healthy prediction is a model classification, not a '
                                            'guarantee that the plant is disease-free.',
                      'management': ['Continue routine crop monitoring and follow locally '
                                     'recommended agronomic practices.',
                                     'If symptoms are visible despite this prediction, obtain a '
                                     'second assessment; the classifier can miss conditions.'],
                      'nutrient_guidance': None,
                      'prevention': ['Use clean planting material, maintain appropriate spacing '
                                     'and irrigation, and monitor plants regularly.'],
                      'review_status': 'REQUIRES_SOURCE_REVIEW',
                      'sources': [],
                      'spread': ['Not applicable to a healthy-class prediction.'],
                      'symptoms': ['The classifier assigned the healthy class. This is not a '
                                   'guarantee that the whole plant is free from disease, pests, or '
                                   'nutrient stress.'],
                      'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                        'prediction.',
                      'type': 'healthy'},
 'Radish___Black_Leaf_Spot': {'causal_agent': None,
                              'chemical_treatment': None,
                              'condition': 'Black Leaf Spot',
                              'crop': 'Radish',
                              'diagnostic_caution': 'The model predicts a dataset label from an '
                                                    'image; it does not confirm the pathogen, '
                                                    'distinguish all look-alike conditions, or '
                                                    'assess disease severity.',
                              'management': ['Inspect more than one plant and compare symptoms '
                                             'with crop-specific guidance from a recognised '
                                             'agricultural-extension service.',
                                             'Remove or isolate affected material only when '
                                             'recommended for the confirmed condition; avoid '
                                             'moving potentially infected planting material.',
                                             'Improve general crop hygiene and avoid unnecessary '
                                             'handling of wet foliage.'],
                              'nutrient_guidance': None,
                              'prevention': ['Use healthy, locally recommended planting material '
                                             'and resistant varieties where available.',
                                             'Monitor the crop regularly and follow crop-specific '
                                             'sanitation and rotation guidance.'],
                              'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                              'sources': [{'organization': 'University of Minnesota Extension',
                                           'title': 'Radish leaf spots: Alternaria black/gray leaf '
                                                    'spot symptoms',
                                           'url': 'https://apps.extension.umn.edu/garden/diagnose/plant/vegetable/radish/leavesspots.html'}],
                              'spread': ['The causal organism and transmission route are not '
                                         'confirmed by the image classifier. Transmission depends '
                                         'on the actual diagnosis.'],
                              'symptoms': ['Discrete spots may appear on leaves and can vary in '
                                           'colour, size, and margin; this broad class does not '
                                           'identify a specific pathogen.'],
                              'treatment_note': 'No chemical treatment is recommended here. '
                                                'Confirm the diagnosis and consult current '
                                                'crop-specific Indian label and registration '
                                                'guidance before any pesticide use.',
                              'type': 'disease_class_unverified'},
 'Radish___Downy_Mildew': {'causal_agent': None,
                           'chemical_treatment': None,
                           'condition': 'Downy Mildew',
                           'crop': 'Radish',
                           'diagnostic_caution': 'The model predicts a dataset label from an '
                                                 'image; it does not confirm the pathogen, '
                                                 'distinguish all look-alike conditions, or assess '
                                                 'disease severity.',
                           'management': ['Inspect more than one plant and compare symptoms with '
                                          'crop-specific guidance from a recognised '
                                          'agricultural-extension service.',
                                          'Remove or isolate affected material only when '
                                          'recommended for the confirmed condition; avoid moving '
                                          'potentially infected planting material.',
                                          'Improve general crop hygiene and avoid unnecessary '
                                          'handling of wet foliage.'],
                           'nutrient_guidance': None,
                           'prevention': ['Use healthy, locally recommended planting material and '
                                          'resistant varieties where available.',
                                          'Monitor the crop regularly and follow crop-specific '
                                          'sanitation and rotation guidance.'],
                           'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                           'sources': [{'organization': 'University of Minnesota Extension',
                                        'title': 'Radish leaf spots: downy mildew symptoms and '
                                                 'cool, wet conditions',
                                        'url': 'https://apps.extension.umn.edu/garden/diagnose/plant/vegetable/radish/leavesspots.html'}],
                           'spread': ['The causal organism and transmission route are not '
                                      'confirmed by the image classifier. Transmission depends on '
                                      'the actual diagnosis.'],
                           'symptoms': ['Yellowish or pale angular patches may appear on upper '
                                        'leaf surfaces, sometimes with downy growth beneath leaves '
                                        'in humid conditions.'],
                           'treatment_note': 'No chemical treatment is recommended here. Confirm '
                                             'the diagnosis and consult current crop-specific '
                                             'Indian label and registration guidance before any '
                                             'pesticide use.',
                           'type': 'oomycete_or_downy_mildew'},
 'Radish___Flea_Beetle': {'causal_agent': None,
                          'chemical_treatment': None,
                          'condition': 'Flea Beetle',
                          'crop': 'Radish',
                          'diagnostic_caution': 'The dataset class indicates '
                                                'flea-beetle-associated damage but does not '
                                                'reliably identify the pest species. Phyllotreta '
                                                'striolata has been documented on radish in India, '
                                                'but this model prediction does not confirm that '
                                                'species. Inspect the plant and obtain field '
                                                'confirmation before taking control action.',
                          'management': ['Inspect both foliage and roots for shot-holes and larval '
                                         'feeding damage before deciding on control.',
                                         'Use an integrated pest-management approach; ICAR-NCIPM '
                                         'reports improved radish crop outcomes from IPM '
                                         'interventions compared with non-IPM fields.',
                                         'Seek local agricultural-extension advice for locally '
                                         'suitable measures; do not select an insecticide from '
                                         'this broad model label.'],
                          'nutrient_guidance': None,
                          'prevention': ['Monitor radish crops regularly for leaf shot-holes and '
                                         'root damage, particularly while plants are developing.',
                                         'Use an integrated management approach rather than '
                                         'routine or unwarranted insecticide applications.',
                                         'Confirm the pest identity before selecting a '
                                         'crop-protection measure.'],
                          'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                          'sources': [{'organization': 'ICAR-National Centre for Integrated Pest '
                                                       'Management',
                                       'title': 'Striped flea beetle, Phyllotreta striolata: '
                                                'status and management in radish',
                                       'url': 'https://epubs.icar.org.in/index.php/IndFarm/article/view/112639'},
                                      {'organization': 'ICAR-Indian Institute of Vegetable '
                                                       'Research',
                                       'title': 'Annual Report 2023–2024 — Biology and organic '
                                                'pest management module for radish flea beetle',
                                       'url': 'https://icariivr.org.in/wp-content/uploads/2025/11/Annual-Report-2023-2024.pdf'}],
                          'spread': ['The specific pest and its movement or life cycle are not '
                                     'identified by this broad image class.'],
                          'symptoms': ['Adult striped flea beetles can produce numerous small '
                                       'shot-holes in radish leaves.',
                                       'Larval feeding can produce dark or black-brown markings on '
                                       'the radish taproot.',
                                       'The model class does not establish the flea-beetle '
                                       'species; confirm the pest by inspecting plants and roots.'],
                          'treatment_note': 'No pesticide is recommended by this classifier. '
                                            "Identify the pest and verify any product's current "
                                            'Indian registration and label before use.',
                          'type': 'pest_or_insect_associated'},
 'Radish___Mosaic': {'causal_agent': 'Radish mosaic virus (dataset-associated label; not confirmed '
                                     'by image classification)',
                     'chemical_treatment': None,
                     'condition': 'Radish mosaic virus disease',
                     'crop': 'Radish',
                     'diagnostic_caution': 'The model predicts a dataset class from an image; it '
                                           'does not confirm Radish mosaic virus or distinguish '
                                           'all look-alike conditions. Confirm uncertain cases '
                                           'through an agricultural-extension service or suitable '
                                           'diagnostic testing.',
                     'management': ['Use disease-free seed or planting material from healthy '
                                    'plants.',
                                    'Remove and dispose of confirmed infected plants according to '
                                    'local crop-health guidance.',
                                    'Monitor for aphids and seek local extension advice for '
                                    'integrated, crop-specific vector management.'],
                     'nutrient_guidance': None,
                     'prevention': ['Use healthy seed or planting material from reliable sources.',
                                    'Inspect crops regularly for mosaic symptoms and aphid '
                                    'activity.',
                                    'Remove confirmed infected plants where recommended to reduce '
                                    'sources of virus.'],
                     'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                     'sources': [{'organization': 'Kerala Agricultural University, Centre for '
                                                  'e-Learning',
                                  'title': 'Radish — Mosaic disease',
                                  'url': 'https://www.celkau.in/Crops/Vegetables/radish/mosaic.php'},
                                 {'organization': 'National Horticulture Board, Government of '
                                                  'India',
                                  'title': 'Radish — Radish Mosaic Virus',
                                  'url': 'https://nhb.gov.in/pdf/vegetable/radish/rad002.pdf'}],
                     'spread': ['Radish mosaic virus is described by agricultural references as '
                                'aphid-transmitted.',
                                'Aphids can move the virus between susceptible plants while '
                                'feeding.',
                                'The image classifier does not detect aphids or confirm virus '
                                'transmission in an individual plant.'],
                     'symptoms': ['Small circular to irregular chlorotic lesions may appear '
                                  'between or adjacent to leaf veins.',
                                  'Leaf distortion may be slight or absent.',
                                  'Affected plants may become stunted; image classification alone '
                                  'cannot confirm the virus.'],
                     'treatment_note': 'No chemical treatment is prescribed. Management focuses on '
                                       'healthy planting material, removal of confirmed infected '
                                       'plants where recommended, and monitoring aphid vectors. Do '
                                       'not infer a pesticide recommendation from this image '
                                       'prediction.',
                     'type': 'viral_disease'},
 'Radish___healthy': {'causal_agent': None,
                      'chemical_treatment': None,
                      'condition': 'healthy',
                      'crop': 'Radish',
                      'diagnostic_caution': 'A healthy prediction is a model classification, not a '
                                            'guarantee that the plant is disease-free.',
                      'management': ['Continue routine crop monitoring and follow locally '
                                     'recommended agronomic practices.',
                                     'If symptoms are visible despite this prediction, obtain a '
                                     'second assessment; the classifier can miss conditions.'],
                      'nutrient_guidance': None,
                      'prevention': ['Use clean planting material, maintain appropriate spacing '
                                     'and irrigation, and monitor plants regularly.'],
                      'review_status': 'REQUIRES_SOURCE_REVIEW',
                      'sources': [],
                      'spread': ['Not applicable to a healthy-class prediction.'],
                      'symptoms': ['The classifier assigned the healthy class. This is not a '
                                   'guarantee that the whole plant is free from disease, pests, or '
                                   'nutrient stress.'],
                      'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                        'prediction.',
                      'type': 'healthy'},
 'Raspberry___healthy': {'causal_agent': None,
                         'chemical_treatment': None,
                         'condition': 'healthy',
                         'crop': 'Raspberry',
                         'diagnostic_caution': 'A healthy prediction is a model classification, '
                                               'not a guarantee that the plant is disease-free.',
                         'management': ['Continue routine crop monitoring and follow locally '
                                        'recommended agronomic practices.',
                                        'If symptoms are visible despite this prediction, obtain a '
                                        'second assessment; the classifier can miss conditions.'],
                         'nutrient_guidance': None,
                         'prevention': ['Use clean planting material, maintain appropriate spacing '
                                        'and irrigation, and monitor plants regularly.'],
                         'review_status': 'REQUIRES_SOURCE_REVIEW',
                         'sources': [],
                         'spread': ['Not applicable to a healthy-class prediction.'],
                         'symptoms': ['The classifier assigned the healthy class. This is not a '
                                      'guarantee that the whole plant is free from disease, pests, '
                                      'or nutrient stress.'],
                         'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                           'prediction.',
                         'type': 'healthy'},
 'Soybean___healthy': {'causal_agent': None,
                       'chemical_treatment': None,
                       'condition': 'healthy',
                       'crop': 'Soybean',
                       'diagnostic_caution': 'A healthy prediction is a model classification, not '
                                             'a guarantee that the plant is disease-free.',
                       'management': ['Continue routine crop monitoring and follow locally '
                                      'recommended agronomic practices.',
                                      'If symptoms are visible despite this prediction, obtain a '
                                      'second assessment; the classifier can miss conditions.'],
                       'nutrient_guidance': None,
                       'prevention': ['Use clean planting material, maintain appropriate spacing '
                                      'and irrigation, and monitor plants regularly.'],
                       'review_status': 'REQUIRES_SOURCE_REVIEW',
                       'sources': [],
                       'spread': ['Not applicable to a healthy-class prediction.'],
                       'symptoms': ['The classifier assigned the healthy class. This is not a '
                                    'guarantee that the whole plant is free from disease, pests, '
                                    'or nutrient stress.'],
                       'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                         'prediction.',
                       'type': 'healthy'},
 'Squash___Powdery_mildew': {'causal_agent': 'Podosphaera xanthii',
                             'chemical_treatment': None,
                             'condition': 'Powdery mildew',
                             'crop': 'Squash',
                             'diagnostic_caution': 'The model predicts a dataset label from an '
                                                   'image; it does not confirm the pathogen, '
                                                   'distinguish all look-alike conditions, or '
                                                   'assess disease severity.',
                             'management': ['Scout older leaves for the first pale spots and '
                                            'powdery colonies rather than waiting for whole leaves '
                                            'to be covered.',
                                            'Remove severely affected leaves where practical to '
                                            'reduce local inoculum and improve canopy conditions.',
                                            'Maintain adequate plant spacing and airflow so '
                                            'infected foliage does not remain in a persistently '
                                            'humid canopy.'],
                             'nutrient_guidance': None,
                             'prevention': ['Grow resistant or tolerant squash cultivars where '
                                            'available for the local production system.',
                                            'Avoid creating excessively dense canopies and '
                                            'excessive nitrogen-driven vegetative growth.',
                                            'Begin scouting before symptoms become widespread '
                                            'because early detection is more useful for managing '
                                            'powdery mildew than removing severely colonized '
                                            'leaves late in the season.'],
                             'review_status': 'REQUIRES_SOURCE_REVIEW',
                             'sources': [{'organization': 'University of Minnesota Extension',
                                          'title': 'Powdery Mildew of Squash and Pumpkins',
                                          'url': 'https://apps.extension.umn.edu/garden/diagnose/plant/vegetable/wintersquash/leavesspots.html'}],
                             'spread': ['Powdery mildew produces airborne spores that can move '
                                        'from infected leaves to healthy leaves and nearby plants.',
                                        'The disease can develop rapidly when susceptible foliage '
                                        'is present and weather favors fungal growth.',
                                        'Older infected leaves can become an important source of '
                                        'spores for subsequent infections.'],
                             'symptoms': ['Pale yellow spots may first appear on older leaves.',
                                          'White to gray powdery fungal growth develops in patches '
                                          'on leaf surfaces and can eventually cover much of the '
                                          'leaf.',
                                          'Severe infection causes leaves and vines to wither and '
                                          'die and can expose fruit to sunscald.'],
                             'treatment_note': 'No chemical treatment is prescribed here; '
                                               'management emphasizes resistant varieties, early '
                                               'detection, canopy conditions and sanitation.',
                             'type': 'Fungal Disease'},
 'Strawberry___Leaf_scorch': {'causal_agent': 'Diplocarpon earlianum',
                              'chemical_treatment': None,
                              'condition': 'Leaf scorch',
                              'crop': 'Strawberry',
                              'diagnostic_caution': 'The model predicts a dataset label from an '
                                                    'image; it does not confirm the pathogen, '
                                                    'distinguish all look-alike conditions, or '
                                                    'assess disease severity.',
                              'management': ['Remove heavily infected leaves and old diseased '
                                             'foliage to reduce local inoculum where practical.',
                                             'Improve airflow around plants and avoid prolonged '
                                             'wetting of foliage during irrigation.',
                                             'Scout new and older leaves for expanding '
                                             'purple-brown lesions and monitor whether disease is '
                                             'increasing after wet periods.'],
                              'nutrient_guidance': None,
                              'prevention': ['Use healthy planting material and maintain adequate '
                                             'spacing between plants.',
                                             'Avoid overhead irrigation where practical so leaves '
                                             'do not remain wet for long periods.',
                                             'Remove diseased foliage and maintain clean beds '
                                             'between production cycles to reduce sources of '
                                             'inoculum.'],
                              'review_status': 'REQUIRES_SOURCE_REVIEW',
                              'sources': [{'organization': 'Penn State Extension',
                                           'title': 'Strawberry Disease Identification',
                                           'url': 'https://extension.psu.edu/strawberry-disease-identification'}],
                              'spread': ['The fungus produces fruiting structures on infected '
                                         'leaves that can release spores under favorable moisture '
                                         'conditions.',
                                         'Rain splash and movement of wet infected foliage can '
                                         'spread spores to nearby leaves.',
                                         'Dense plantings and prolonged leaf wetness increase '
                                         'opportunities for infection and secondary spread.'],
                              'symptoms': ['Irregular purple to brown leaf blotches develop, with '
                                           'surrounding tissue becoming purple to red.',
                                           'Black, disc-shaped fungal fruiting structures can '
                                           'develop on the upper leaf surface.',
                                           'Severe infection reduces healthy leaf area and can '
                                           'cause extensive leaf discoloration.'],
                              'treatment_note': 'No chemical treatment is prescribed here; '
                                                'management focuses on sanitation, reduced leaf '
                                                'wetness and maintaining airflow around strawberry '
                                                'foliage.',
                              'type': 'Fungal Disease'},
 'Strawberry___healthy': {'causal_agent': None,
                          'chemical_treatment': None,
                          'condition': 'healthy',
                          'crop': 'Strawberry',
                          'diagnostic_caution': 'A healthy prediction is a model classification, '
                                                'not a guarantee that the plant is disease-free.',
                          'management': ['Continue routine crop monitoring and follow locally '
                                         'recommended agronomic practices.',
                                         'If symptoms are visible despite this prediction, obtain '
                                         'a second assessment; the classifier can miss '
                                         'conditions.'],
                          'nutrient_guidance': None,
                          'prevention': ['Use clean planting material, maintain appropriate '
                                         'spacing and irrigation, and monitor plants regularly.'],
                          'review_status': 'REQUIRES_SOURCE_REVIEW',
                          'sources': [],
                          'spread': ['Not applicable to a healthy-class prediction.'],
                          'symptoms': ['The classifier assigned the healthy class. This is not a '
                                       'guarantee that the whole plant is free from disease, '
                                       'pests, or nutrient stress.'],
                          'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                            'prediction.',
                          'type': 'healthy'},
 'Tomato___Bacterial_spot': {'causal_agent': 'Xanthomonas spp. causing bacterial spot (TNAU '
                                             'identifies Xanthomonas axonopodis pv. vesicatoria; '
                                             'taxonomy may vary among the bacterial-spot complex)',
                             'chemical_treatment': None,
                             'condition': 'Bacterial spot',
                             'crop': 'Tomato',
                             'diagnostic_caution': 'The model predicts a dataset label from an '
                                                   'image; it does not confirm the pathogen, '
                                                   'distinguish all look-alike conditions, or '
                                                   'assess disease severity.',
                             'management': ['Inspect more than one plant and compare symptoms with '
                                            'crop-specific guidance from a recognised '
                                            'agricultural-extension service.',
                                            'Remove or isolate affected material only when '
                                            'recommended for the confirmed condition; avoid moving '
                                            'potentially infected planting material.',
                                            'Improve general crop hygiene and avoid unnecessary '
                                            'handling of wet foliage.'],
                             'nutrient_guidance': None,
                             'prevention': ['Use healthy, locally recommended planting material '
                                            'and resistant varieties where available.',
                                            'Monitor the crop regularly and follow crop-specific '
                                            'sanitation and rotation guidance.'],
                             'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                             'sources': [{'organization': 'Tamil Nadu Agricultural University '
                                                          '(TNAU) Agritech Portal',
                                          'title': 'Tomato bacterial leaf spot: symptoms, causal '
                                                   'organism and spread',
                                          'url': 'https://agritech.tnau.ac.in/crop_protection/tomato_diseases_11.html'}],
                             'spread': ['TNAU describes survival in infected debris, primary '
                                        'spread through infected debris and seed, and secondary '
                                        'spread by rain splash. Moist weather and persistent dew '
                                        'favour disease.'],
                             'symptoms': ['Small brown, water-soaked circular leaf spots may '
                                          'develop, sometimes with yellow halos; green fruit can '
                                          'develop water-soaked, later scabby spots.'],
                             'treatment_note': 'No chemical treatment is recommended here. Confirm '
                                               'the diagnosis and consult current crop-specific '
                                               'Indian label and registration guidance before any '
                                               'pesticide use.',
                             'type': 'bacterial_disease'},
 'Tomato___Early_blight': {'causal_agent': 'Alternaria solani',
                           'chemical_treatment': None,
                           'condition': 'Early blight',
                           'crop': 'Tomato',
                           'diagnostic_caution': 'The model predicts a dataset label from an '
                                                 'image; it does not confirm the pathogen, '
                                                 'distinguish all look-alike conditions, or assess '
                                                 'disease severity. Confirm uncertain cases with a '
                                                 'qualified plant-health professional.',
                           'management': ['Use healthy, disease-free seed and inspect older/lower '
                                          'leaves regularly.',
                                          'Remove and appropriately dispose of infected crop '
                                          'debris after harvest; avoid carrying contaminated plant '
                                          'material between fields.',
                                          'Use crop rotation with non-solanaceous crops and '
                                          'maintain suitable plant spacing and canopy aeration.',
                                          'Avoid prolonged leaf wetness and manage irrigation to '
                                          'reduce unnecessary wetting of foliage.'],
                           'nutrient_guidance': None,
                           'prevention': ['Start with healthy seed or seedlings and maintain field '
                                          'sanitation.',
                                          'Rotate away from tomato and other solanaceous crops '
                                          'where practical; monitor the crop, especially during '
                                          'warm, humid and wet periods.'],
                           'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                           'sources': [{'organization': 'Tamil Nadu Agricultural University (TNAU) '
                                                        'Agritech Portal',
                                        'title': 'Tomato early blight: Alternaria solani, '
                                                 'symptoms, survival, spread and integrated '
                                                 'disease management',
                                        'url': 'https://agritech.tnau.ac.in/crop_protection/tomato_diseases_2.html'}],
                           'spread': ['The fungus can survive in infected crop debris; infected '
                                      'seed may contribute to primary infection.',
                                      'Spores can spread by wind and rain splash. Warm, humid '
                                      'conditions and prolonged leaf wetness favour disease '
                                      'development.'],
                           'symptoms': ['Small brown to dark lesions may first appear on older '
                                        'leaves; lesions often develop concentric rings (a '
                                        'target-like pattern) and may have a yellow margin.',
                                        'As lesions enlarge and coalesce, leaves may yellow and '
                                        'die; stems and fruit near the calyx can also develop '
                                        'dark, concentric lesions.'],
                           'treatment_note': 'No chemical treatment is prescribed by this '
                                             'educational entry. Confirm the diagnosis and consult '
                                             'current local agricultural-extension guidance and '
                                             'the applicable Indian product label before '
                                             'considering any crop-protection product.',
                           'type': 'fungal_disease'},
 'Tomato___Late_blight': {'causal_agent': 'Phytophthora infestans',
                          'chemical_treatment': None,
                          'condition': 'Late blight',
                          'crop': 'Tomato',
                          'diagnostic_caution': 'The model predicts a dataset label from an image; '
                                                'it does not confirm the pathogen, distinguish all '
                                                'look-alike conditions, or assess disease '
                                                'severity.',
                          'management': ['Inspect more than one plant and compare symptoms with '
                                         'crop-specific guidance from a recognised '
                                         'agricultural-extension service.',
                                         'Remove or isolate affected material only when '
                                         'recommended for the confirmed condition; avoid moving '
                                         'potentially infected planting material.',
                                         'Improve general crop hygiene and avoid unnecessary '
                                         'handling of wet foliage.'],
                          'nutrient_guidance': None,
                          'prevention': ['Use healthy, locally recommended planting material and '
                                         'resistant varieties where available.',
                                         'Monitor the crop regularly and follow crop-specific '
                                         'sanitation and rotation guidance.'],
                          'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                          'sources': [{'organization': 'Tamil Nadu Agricultural University (TNAU) '
                                                       'Agritech Portal',
                                       'title': 'Tomato late blight: Phytophthora infestans, '
                                                'symptoms and spread',
                                       'url': 'https://agritech.tnau.ac.in/crop_protection/tomato_diseases_8.html'}],
                          'spread': ['TNAU describes survival in infected debris and secondary '
                                     'spread by wind. Cool nights, warm days and extended leaf '
                                     'wetness from rain or fog favour disease development.'],
                          'symptoms': ['Water-soaked dark lesions may develop on leaves and stems '
                                       'and expand rapidly; white sporulation may be visible on '
                                       'leaf tissue in humid conditions. Fruit can develop dark, '
                                       'firm lesions and soft rot.'],
                          'treatment_note': 'No chemical treatment is recommended here. Confirm '
                                            'the diagnosis and consult current crop-specific '
                                            'Indian label and registration guidance before any '
                                            'pesticide use.',
                          'type': 'oomycete_or_downy_mildew'},
 'Tomato___Leaf_Mold': {'causal_agent': None,
                        'chemical_treatment': None,
                        'condition': 'Leaf Mold',
                        'crop': 'Tomato',
                        'diagnostic_caution': 'The model predicts a dataset label from an image; '
                                              'it does not confirm the pathogen, distinguish all '
                                              'look-alike conditions, or assess disease severity.',
                        'management': ['Inspect more than one plant and compare symptoms with '
                                       'crop-specific guidance from a recognised '
                                       'agricultural-extension service.',
                                       'Remove or isolate affected material only when recommended '
                                       'for the confirmed condition; avoid moving potentially '
                                       'infected planting material.',
                                       'Improve general crop hygiene and avoid unnecessary '
                                       'handling of wet foliage.'],
                        'nutrient_guidance': None,
                        'prevention': ['Use healthy, locally recommended planting material and '
                                       'resistant varieties where available.',
                                       'Monitor the crop regularly and follow crop-specific '
                                       'sanitation and rotation guidance.'],
                        'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                        'sources': [{'organization': 'University of Minnesota Extension',
                                     'title': 'Tomato leaf mold: Passalora fulva, symptoms, '
                                              'humidity and spread',
                                     'url': 'https://extension.umn.edu/agriculture/specialty-crops/vegetable-farming/disease-management/tomato-leaf-mold'}],
                        'spread': ['The causal organism and transmission route are not confirmed '
                                   'by the image classifier. Transmission depends on the actual '
                                   'diagnosis.'],
                        'symptoms': ['Yellow patches may develop on upper leaf surfaces with '
                                     'olive-green to brown mould-like growth underneath in humid '
                                     'conditions.'],
                        'treatment_note': 'No chemical treatment is recommended here. Confirm the '
                                          'diagnosis and consult current crop-specific Indian '
                                          'label and registration guidance before any pesticide '
                                          'use.',
                        'type': 'disease_class_unverified'},
 'Tomato___Septoria_leaf_spot': {'causal_agent': 'Septoria lycopersici',
                                 'chemical_treatment': None,
                                 'condition': 'Septoria leaf spot',
                                 'crop': 'Tomato',
                                 'diagnostic_caution': 'The model predicts a dataset label from an '
                                                       'image; it does not confirm the pathogen, '
                                                       'distinguish all look-alike conditions, or '
                                                       'assess disease severity.',
                                 'management': ['Inspect more than one plant and compare symptoms '
                                                'with crop-specific guidance from a recognised '
                                                'agricultural-extension service.',
                                                'Remove or isolate affected material only when '
                                                'recommended for the confirmed condition; avoid '
                                                'moving potentially infected planting material.',
                                                'Improve general crop hygiene and avoid '
                                                'unnecessary handling of wet foliage.'],
                                 'nutrient_guidance': None,
                                 'prevention': ['Use healthy, locally recommended planting '
                                                'material and resistant varieties where available.',
                                                'Monitor the crop regularly and follow '
                                                'crop-specific sanitation and rotation guidance.'],
                                 'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                                 'sources': [{'organization': 'Tamil Nadu Agricultural University '
                                                              '(TNAU) Agritech Portal',
                                              'title': 'Tomato Septoria leaf spot: Septoria '
                                                       'lycopersici, symptoms and spread',
                                              'url': 'https://agritech.tnau.ac.in/crop_protection/tomato_diseases_4.html'}],
                                 'spread': ['The pathogen can survive in infected plant debris. '
                                            'Conidia can spread through rain splash and wind, '
                                            'especially under humid conditions.'],
                                 'symptoms': ['Small round to irregular leaf spots may have grey '
                                              'centres and dark margins; lesions can merge, blight '
                                              'leaves and cause defoliation.'],
                                 'treatment_note': 'No chemical treatment is recommended here. '
                                                   'Confirm the diagnosis and consult current '
                                                   'crop-specific Indian label and registration '
                                                   'guidance before any pesticide use.',
                                 'type': 'fungal_disease'},
 'Tomato___Spider_mites Two-spotted_spider_mite': {'causal_agent': 'Two-spotted spider mite '
                                                                   '(Tetranychus urticae); visual '
                                                                   'identification to species '
                                                                   'requires examination',
                                                   'chemical_treatment': None,
                                                   'condition': 'Spider mites Two-spotted spider '
                                                                'mite',
                                                   'crop': 'Tomato',
                                                   'diagnostic_caution': 'The model predicts a '
                                                                         'dataset label from an '
                                                                         'image; it does not '
                                                                         'confirm the pathogen, '
                                                                         'distinguish all '
                                                                         'look-alike conditions, '
                                                                         'or assess disease '
                                                                         'severity. Confirm '
                                                                         'uncertain cases with a '
                                                                         'qualified plant-health '
                                                                         'professional.',
                                                   'management': ['Inspect the undersides of '
                                                                  'leaves with a hand lens for '
                                                                  'mites, eggs and webbing before '
                                                                  'deciding on management.',
                                                                  'Conserve natural enemies where '
                                                                  'possible and seek local '
                                                                  'integrated pest-management '
                                                                  'advice for confirmed '
                                                                  'infestations.',
                                                                  'Avoid broad-spectrum pesticide '
                                                                  'use without diagnosis, as it '
                                                                  'may disrupt natural mite '
                                                                  'predators.'],
                                                   'nutrient_guidance': None,
                                                   'prevention': ['Inspect incoming seedlings and '
                                                                  'monitor leaf undersides '
                                                                  'regularly, especially in hot, '
                                                                  'dry conditions.',
                                                                  'Reduce movement of infested '
                                                                  'plant material and maintain '
                                                                  'appropriate crop hygiene.'],
                                                   'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                                                   'sources': [{'organization': 'Tamil Nadu '
                                                                                'Agricultural '
                                                                                'University (TNAU) '
                                                                                'Agritech Portal',
                                                                'title': 'Tomato red spider mite: '
                                                                         'Tetranychus spp., '
                                                                         'symptoms and '
                                                                         'identification',
                                                                'url': 'https://agritech.tnau.ac.in/crop_protection/tomato/tomato_7.html'}],
                                                   'spread': ['Spider mites can spread between '
                                                              'plants by crawling and may be '
                                                              'dispersed by wind, people, tools or '
                                                              'infested plant material. The TNAU '
                                                              'tomato pest page identifies red '
                                                              'spider mites as Tetranychus spp.; '
                                                              'it does not establish species from '
                                                              'an image.'],
                                                   'symptoms': ['Mite feeding can cause fine '
                                                                'stippling, bronzing or '
                                                                'reddish-brown discolouration of '
                                                                'leaves. Heavy infestations may '
                                                                'produce webbing, leaf drying and '
                                                                'reduced plant vigour.'],
                                                   'treatment_note': 'No chemical treatment is '
                                                                     'prescribed by this '
                                                                     'educational entry. Confirm '
                                                                     'the diagnosis and consult '
                                                                     'current local '
                                                                     'agricultural-extension '
                                                                     'guidance and applicable '
                                                                     'Indian product-label '
                                                                     'requirements before '
                                                                     'considering any '
                                                                     'crop-protection product.',
                                                   'type': 'arthropod_pest'},
 'Tomato___Target_Spot': {'causal_agent': 'Corynespora cassiicola (reported cause of tomato target '
                                          'spot; image prediction alone does not confirm '
                                          'infection).',
                          'chemical_treatment': None,
                          'condition': 'Target Spot',
                          'crop': 'Tomato',
                          'diagnostic_caution': 'The model predicts a dataset label from an image; '
                                                'it does not confirm the pathogen, distinguish all '
                                                'look-alike conditions, or assess disease '
                                                'severity.',
                          'management': ['Confirm the diagnosis because target spot resembles '
                                         'other tomato leaf diseases.',
                                         'Use good airflow, avoid prolonged leaf wetness, and '
                                         'manage crop residues according to local extension '
                                         'advice.',
                                         'No chemical product or dose is recommended in this '
                                         'entry.'],
                          'nutrient_guidance': None,
                          'prevention': ['Use healthy, locally recommended planting material and '
                                         'resistant varieties where available.',
                                         'Monitor the crop regularly and follow crop-specific '
                                         'sanitation and rotation guidance.'],
                          'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                          'sources': [{'organization': 'University of Florida IFAS Extension',
                                       'title': 'Target spot of tomato: Corynespora cassiicola, '
                                                'symptoms and epidemiology',
                                       'url': 'https://ask.ifas.ufl.edu/publication/PP351'}],
                          'spread': ['The UF/IFAS source describes spores dispersed by wind and '
                                     'rain; prolonged leaf wetness and humid conditions favour '
                                     'infection.'],
                          'symptoms': ['Small dark or water-soaked leaf lesions may enlarge into '
                                       'light-brown to grey centres with darker concentric margins '
                                       'and sometimes yellowing.',
                                       'Lesions can merge and cause blighting; stems and fruit may '
                                       'also develop lesions. Similar patterns occur in early '
                                       'blight and bacterial spot.'],
                          'treatment_note': 'No chemical treatment is recommended here. Confirm '
                                            'the diagnosis and consult current crop-specific '
                                            'Indian label and registration guidance before any '
                                            'pesticide use.',
                          'type': 'disease_class_unverified'},
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {'causal_agent': 'Begomoviruses associated with tomato '
                                                            'yellow leaf curl disease (TYLCV '
                                                            'complex; the exact virus '
                                                            'species/strain varies by region)',
                                            'chemical_treatment': None,
                                            'condition': 'Tomato Yellow Leaf Curl Virus',
                                            'crop': 'Tomato',
                                            'diagnostic_caution': 'The model predicts a dataset '
                                                                  'label from an image; it does '
                                                                  'not confirm the pathogen, '
                                                                  'distinguish all look-alike '
                                                                  'conditions, or assess disease '
                                                                  'severity. Confirm uncertain '
                                                                  'cases with a qualified '
                                                                  'plant-health professional.',
                                            'management': ['Seek plant-health confirmation where '
                                                           'the diagnosis affects crop decisions.',
                                                           'Remove and safely dispose of confirmed '
                                                           'infected plants according to local '
                                                           'extension advice.',
                                                           'Use integrated whitefly management '
                                                           'only when locally recommended; do not '
                                                           'apply insecticides solely because of '
                                                           'an image prediction.'],
                                            'nutrient_guidance': None,
                                            'prevention': ['Use healthy seedlings and protected '
                                                           'nursery practices where suitable.',
                                                           'Monitor whiteflies and remove weed '
                                                           'hosts based on local extension '
                                                           'recommendations.',
                                                           'Avoid moving suspect seedlings or '
                                                           'plant material between fields.'],
                                            'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                                            'sources': [{'organization': 'Tamil Nadu Agricultural '
                                                                         'University (TNAU) '
                                                                         'Agritech Portal',
                                                         'title': 'Tomato leaf curl: symptoms, '
                                                                  'Tomato leaf curl virus and '
                                                                  'Bemisia tabaci vector',
                                                         'url': 'https://agritech.tnau.ac.in/crop_protection/tomato_diseases_6.html'}],
                                            'spread': ['TNAU identifies the whitefly Bemisia '
                                                       'tabaci as the principal vector and '
                                                       'movement of infected plants as another '
                                                       'route of spread. The specific begomovirus '
                                                       'species should not be inferred from leaf '
                                                       'appearance.'],
                                            'symptoms': ['Severe stunting, downward curling and '
                                                         'crinkling of leaves, yellowing of newly '
                                                         'emerging leaves, shortened internodes '
                                                         'and a bushy appearance may occur. Early '
                                                         'infection can greatly reduce flowering '
                                                         'and fruiting.'],
                                            'treatment_note': 'No chemical treatment is prescribed '
                                                              'by this educational entry. Confirm '
                                                              'the diagnosis and consult current '
                                                              'local agricultural-extension '
                                                              'guidance and applicable Indian '
                                                              'product-label requirements before '
                                                              'considering any crop-protection '
                                                              'product.',
                                            'type': 'viral_disease'},
 'Tomato___Tomato_mosaic_virus': {'causal_agent': 'Tomato mosaic virus (ToMV) is the dataset class '
                                                  'association; similar symptoms can be caused by '
                                                  'other tomato viruses and laboratory '
                                                  'confirmation is required.',
                                  'chemical_treatment': None,
                                  'condition': 'Tomato mosaic virus',
                                  'crop': 'Tomato',
                                  'diagnostic_caution': 'The model predicts a dataset label from '
                                                        'an image; it does not confirm the '
                                                        'pathogen, distinguish all look-alike '
                                                        'conditions, or assess disease severity.',
                                  'management': ['Obtain laboratory or qualified plant-pathology '
                                                 'confirmation because different viruses produce '
                                                 'overlapping symptoms.',
                                                 'For confirmed ToMV, use clean seed/transplants, '
                                                 'clean hands and tools, and remove confirmed '
                                                 'infected plants according to local guidance.',
                                                 'There is no curative treatment for an infected '
                                                 'plant; do not use insecticides unless a specific '
                                                 'insect-vector problem is independently '
                                                 'identified.'],
                                  'nutrient_guidance': None,
                                  'prevention': ['Use healthy, locally recommended planting '
                                                 'material and resistant varieties where '
                                                 'available.',
                                                 'Monitor the crop regularly and follow '
                                                 'crop-specific sanitation and rotation guidance.'],
                                  'review_status': 'PARTIALLY_SOURCE_SUPPORTED',
                                  'sources': [{'organization': 'University of Minnesota Extension',
                                               'title': 'Tomato viruses: tomato mosaic virus, '
                                                        'overlapping symptoms and need for '
                                                        'laboratory confirmation',
                                               'url': 'https://extension.umn.edu/agriculture/specialty-crops/vegetable-farming/disease-management/tomato-viruses'}],
                                  'spread': ['Tomato viruses differ in their transmission routes. '
                                             'ToMV and related tobamoviruses can spread '
                                             'mechanically through contaminated hands, tools and '
                                             'plant material; the cited extension source also '
                                             'discusses seed and other virus-specific routes.'],
                                  'symptoms': ['Light and dark green mosaic patterns, leaf '
                                               'distortion, and stunting may occur.'],
                                  'treatment_note': 'There is no curative antiviral pesticide '
                                                    'recommendation in this knowledge base. '
                                                    'Management depends on confirmed diagnosis '
                                                    'and, where relevant, vector control.',
                                  'type': 'viral_disease'},
 'Tomato___healthy': {'causal_agent': None,
                      'chemical_treatment': None,
                      'condition': 'healthy',
                      'crop': 'Tomato',
                      'diagnostic_caution': 'A healthy prediction is a model classification, not a '
                                            'guarantee that the plant is disease-free.',
                      'management': ['Continue routine crop monitoring and follow locally '
                                     'recommended agronomic practices.',
                                     'If symptoms are visible despite this prediction, obtain a '
                                     'second assessment; the classifier can miss conditions.'],
                      'nutrient_guidance': None,
                      'prevention': ['Use clean planting material, maintain appropriate spacing '
                                     'and irrigation, and monitor plants regularly.'],
                      'review_status': 'REQUIRES_SOURCE_REVIEW',
                      'sources': [],
                      'spread': ['Not applicable to a healthy-class prediction.'],
                      'symptoms': ['The classifier assigned the healthy class. This is not a '
                                   'guarantee that the whole plant is free from disease, pests, or '
                                   'nutrient stress.'],
                      'treatment_note': 'No disease treatment is indicated by a healthy-class '
                                        'prediction.',
                      'type': 'healthy'}}

def get_knowledge(class_name: str):
    """Return the knowledge-base entry for an exact model class key."""
    return KNOWLEDGE_BASE.get(class_name)

def validate_knowledge_base(expected_class_names=None):
    """Validate key coverage and safety invariants; return a list of errors."""
    errors = []
    if expected_class_names is not None:
        expected = set(expected_class_names)
        actual = set(KNOWLEDGE_BASE)
        for key in sorted(expected - actual):
            errors.append(f"Missing knowledge entry: {key}")
        for key in sorted(actual - expected):
            errors.append(f"Unexpected knowledge entry: {key}")
    for key, entry in KNOWLEDGE_BASE.items():
        required = {"crop", "condition", "type", "causal_agent", "symptoms", "spread", "management", "prevention", "chemical_treatment", "treatment_note", "diagnostic_caution", "nutrient_guidance", "sources", "review_status"}
        missing = required - set(entry)
        if missing:
            errors.append(f"{key}: missing fields {sorted(missing)}")
        if key.endswith("___healthy"):
            if entry.get("chemical_treatment") is not None:
                errors.append(f"{key}: healthy class must not have chemical treatment")
            if "healthy" not in entry.get("type", ""):
                errors.append(f"{key}: healthy class has incorrect type")
        if entry.get("chemical_treatment") is not None and not entry.get("sources"):
            errors.append(f"{key}: chemical treatment has no supporting source")
    return errors
