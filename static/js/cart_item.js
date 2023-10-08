function toggleConfirmation(toyId) {
    const confirmDiv = document.getElementById(`confirmation-${toyId}`);
    const deleteIcon = document.getElementById(`delete-button-${toyId}`);
    
    if (confirmDiv.classList.contains('hidden')) {
        // If the confirmation is hidden, show it and disable the delete icon.
        confirmDiv.classList.remove('hidden');
        deleteIcon.classList.add('text-zinc-400');
        deleteIcon.classList.remove('text-zinc-800', 'hover:text-red-600');
        deleteIcon.style.pointerEvents = 'none'; // Disable clicking on it
    } else {
        // If the confirmation is showing, hide it and restore the delete icon.
        confirmDiv.classList.add('hidden');
        deleteIcon.classList.remove('text-zinc-400');
        deleteIcon.classList.add('text-zinc-800', 'hover:text-red-600');
        deleteIcon.style.pointerEvents = 'auto'; // Enable clicking on it
    }
}