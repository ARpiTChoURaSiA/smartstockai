def calculate_reorder_quantity(current_qty: int, threshold: int, desired: int) -> int:
    """Simple helper to compute reorder amount."""
    if current_qty >= threshold:
        return 0
    return max(0, desired - current_qty)
