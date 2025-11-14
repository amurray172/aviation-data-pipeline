

from models import Contact


def filter_ground_contacts(contacts: list[Contact]) -> str:
    """Filters out ground contacts to ensure we only capture airborne vehicles (above 500ft)."""
    filtered_contacts = []
    for contact in contacts:
        if contact.on_ground is True:
            continue
        if contact.baro_altitude is None:
            continue
        if contact.baro_altitude < 152.4:  # omit contacts below 500ft (152.4 meters)
            continue
        filtered_contacts.append(contact)
    return filtered_contacts



def filter_emergency_contacts(contacts: list[Contact]) -> list[Contact]:
    """Filters contacts to only include those in emergency squawk codes."""
    emergency_contacts = []
    for contact in contacts:
        if contact.squawk in {"7500", "7600", "7700"}:
            emergency_contacts.append(contact)
    return emergency_contacts