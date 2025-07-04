function mostrarZona(zona) {
    const mapa = document.getElementById("mapa-img");

    switch(zona) {
        case 'general':
            mapa.src = "/static/mapa/mapa_general.png";
            break;
        case 'sur':
            mapa.src = "/static/mapa/mapa_zona_sur.png";
            break;
        case 'norte':
            mapa.src = "/static/mapa/mapa_zona_norte.png";
            break;
        default:
            mapa.src = "/static/mapa/mapa_general.png";
    }
}
