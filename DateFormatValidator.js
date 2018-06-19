// Using regex
function dateFormatValidator(date){
    patt = /\d\d.\d\d.\d\d\d\d/i
    if (date.search(patt) == -1){

        return "False"
    }
    else{

        return "True"
    }
}
