function classificacao(vitorias = 0){
    if (vitorias < 10){
        return 'Ferro'}
    else if (vitorias < 21){
        return 'Bronze'}
    else if (vitorias < 51){
        return 'Prata'}
    else if (vitorias < 71){
        return 'Ouro'}
    else if (vitorias < 81){
        return 'Platina'}
    else if (vitorias < 91){
        return 'Ascendente'}
    else if (vitorias < 101){
        return 'Imortal'}
    else if (vitorias > 101){
        return 'Radiante'}
}

function calcular(){
    let vit = document.getElementById('vitorias').value;
    let der = document.getElementById('derrotas').value;
    let resp = document.getElementById('rensponse');
    let saldo = classificacao(vit - der);
    resp.insertAdjacentHTML('beforebegin','<center>\
    <h2>O Herói com o saldo de '+vit +' vitórias</h2>' +
    '<h1>Ele está no nível de '+saldo+'</h1></center>');
}