import re
def Language_req(description):
    """Create a function that captures the language requirements from the job description"""
    description = description.lower()
    matches = re.findall(r"\benglish\sand\sgerman\b|\bgerman\sand\senglish\b\benglisch\sund\sdeutsch\b|\benglish\b|\benglisch\b|\bgerman\b|\bdeutsch\b", description)
    for item in matches:
        return item
  