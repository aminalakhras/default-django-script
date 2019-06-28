from . import settings

# checks if the vlaue in defined or not
# the value is returned if it's defined, and None is return if it doesn't exist
def exists_or_None(dictionary_as_string, variblable_as_string):
    try:
        result = eval(f"""{dictionary_as_string}.{variblable_as_string}""")
        return result
    except AttributeError as e:
        print("Attribute Error at templatesGlobalSettings:", e)
        return None

# variables appear in the templates as global variables and they're brought from the settings.py file
def adminCustomeSettingsForTemplates(request):
    return {
        'useGoogleAnalytics': exists_or_None("settings","useGoogleAnalytics"),
        "googleAnalyticsID" : exists_or_None("settings","googleAnalyticsID"),

        }
