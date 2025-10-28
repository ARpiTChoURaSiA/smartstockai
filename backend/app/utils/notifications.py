ṅef send_notification(to: str, subject: str, message: str) -> bool:
    """Placeholder notification sender (no-op)."""
    # integrate email/sms/push later
    print(f"Notify {to}: {subject} - {message}")
    return True
