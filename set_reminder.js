function setReminder() {
    var selectedNote = document.querySelector('.note.selected');
    if (selectedNote) {
        var noteText = selectedNote.innerText;
        var url = `https://calendar.google.com/calendar/r/eventedit?text=${encodeURIComponent(noteText)}`;

        var iframe = document.createElement('iframe');
        iframe.setAttribute('src', url);
        iframe.style.position = 'fixed';
        iframe.style.bottom = '10px';
        iframe.style.right = '10px';
        iframe.style.width = '300px';
        iframe.style.height = '400px';
        iframe.style.border = 'none';

        var container = document.getElementById('calendar-container');
        container.innerHTML = ''; // Clear any existing iframe
        container.appendChild(iframe);

        showMessage('Google Calendar opened for setting reminder.', 'green');
    } else {
        showMessage('Please select a note.', 'red');
    }
}





function selectNote(noteElement) {
    var notes = document.querySelectorAll('.note');
    notes.forEach(function(note) {
        note.classList.remove('selected');
    });
    noteElement.classList.add('selected');
}
function addNote() {
    var noteText = document.getElementById('note-entry').value.trim();
    if (noteText !== '') {
        var div = document.createElement('div');
        div.innerText = noteText;
        div.classList.add('note');
        document.getElementById('notes-list').appendChild(div);
        document.getElementById('note-entry').value = '';
        showMessage('Note added successfully.', 'green');
    } else {
        showMessage('Please enter a note.', 'red');
    }
}
