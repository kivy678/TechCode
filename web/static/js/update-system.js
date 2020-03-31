$(document).ready(function(){
    $('form[us-target="form"]').submit(function(){
        check = true;
        $(this).find('input[us-target="form-data"]').each(function(){
            if(check === false) return;
            check = $(this).val().trim().length > 0;
        });
        if(!check) {
            alert('입력 값이 비어있습니다.');
            return false;
        }
            
        return true;
    });
    $('form[us-target="hash-form-check"]').submit(function(){
        check = true;
        var matcher = /^[a-fA-F0-9]+$/;
        $(this).find('input[us-target="hash-check"]').each(function(){
            if(false === check) return;
            var val = $(this).val().trim();
            if($(this).attr('maxlength') != val.length) {
                check=false;
                return;
            }
            if(null === val.match(matcher))
                check=false;
        });
        if(!check) {
            alert('해시 데이터가 잘못되어 있습니다.');
            return false;
        }
        return true;
    });
});
