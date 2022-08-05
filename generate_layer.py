import json

technique_list = ['T1069','T1018']

layer_dict = {"name": "Relevant Attack Pattern Selection", "version": {"attack": "8", "navigator": "4.0", "layer": "4.0"}, "domain": "enterprise-attack", "description": "This custom layer contains all relevant attack pattern for the given selection criteria.", "filters": {
		"platforms": [
			"Linux",
			"macOS",
			"Windows",
			"Office 365",
			"Azure AD",
			"AWS",
			"GCP",
			"Azure",
			"SaaS",
			"PRE",
			"Network"
		]
	},
	"sorting": 0,
	"layout": {
		"layout": "side",
		"showID": False,
		"showName": True
	},
	"hideDisabled": False,
	"techniques": [],
	"gradient": {
		"colors": [
			"#ffffff",
			"#66b1ff"
		],
		"minValue": 0,
		"maxValue": 1
	},
	"legendItems": [
		{
			"color": "#66b1ff",
			"label": "used by Wizard Spider"
		},
		{
			"color": "#a1d99b",
			"label": "New Wizard Spider techniques as of Nov 2020 "
		}
	],
	"metadata": [],
	"showTacticRowBackground": False,
	"tacticRowBackground": "#dddddd",
	"selectTechniquesAcrossTactics": True,
	"selectSubtechniquesWithParent": False }

for technique in technique_list:
    # Generate the layer for the technique
    layer_dict["techniques"].append({"techniqueID": technique, "tactic": "Discovery", "score": 1, "color": "", "comment": "Test Comment", "enabled": True, "metadata": "", "showSubtechniques": False})


# write layer_dict to json file
with open('layer.json', 'w') as outfile:
    json.dump(layer_dict, outfile)
