$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data, textStatus) => {
    if (textStatus === 'success') {
        $('#character').text(data.name);
    }
}); 