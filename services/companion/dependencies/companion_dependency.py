from companion.use_cases.companion_service import Companion

companion_instance = Companion()

def call_companion_service():
    return companion_instance.chat