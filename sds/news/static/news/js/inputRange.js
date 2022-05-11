(function(){
 
    document.querySelectorAll("input[type='range']").forEach((rangeInput )=> {
        let price = rangeInput.closest('.range__container').querySelector('.range__value');
        let ending
        if (rangeInput.getAttribute('id') === 'rangePriceInput'){
            ending = "₽"
        } else if (rangeInput.getAttribute('id') === 'rangeDiagonalInput'){
            ending = "\""
        } else if (rangeInput.getAttribute('id') === 'rangeRamInput'){
            ending = " ГБ"
        } else if (rangeInput.getAttribute('id') === 'rangeRomInput'){
            ending = " ГБ"
        } else if (rangeInput.getAttribute('id') === 'rangeBatteryInput'){
            ending = " мАч"
        } else if (rangeInput.getAttribute('id') === 'rangeProcessorInput'){
            ending = " ГГц"
        } else if (rangeInput.getAttribute('id') === 'rangeWarrantyInput'){
            ending = " мес."
        } 
        rangeInput.addEventListener('input', () => {
            price.innerText = rangeInput.value + ending;
        });
    });
    
})();