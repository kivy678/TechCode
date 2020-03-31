$(document).ready(function(){

    var nanCheck = function(a,b){ var v = parseInt(a); if(isNaN(v)) return b; else return v; }
        
    var uaForm = $('form[us-target="update-form"]');
    var spTotal = uaForm.find('span#total');
    var updateTotal = function(){
        var total = 0;
        $('span[us-target="field-summary"]').each(function(){
            total += nanCheck($(this).text(), 0);
        });
        spTotal.text(total);
    };
                  
    uaForm.submit(function(){
        var descText = '패턴 종류별 종합집계\n';

        d3.nest()
            .key(function(d){ return d.name; })
            .entries($('span[us-target="field-summary"]')
                     .map(function(d){
                         return {
                             name: $(this).attr('us-data-name'),
                             val:  nanCheck($(this).text(), 0)
                         };
                     }))
            .map(function(d){
                var k = d.key;
                var v = 0;
                
                d.values.map(function(d){
                    v += nanCheck(d.val);
                });

                if(0 === v) return;
                descText += k + ': ' + v + '\n'
            });

        return confirm('업데이트 추가 패턴은 총 ' + spTotal.text() + ' 입니다. \n' + descText + '\n업데이트 패턴 정보를 등록하시겠습니까?');
    }).ready(
        updateTotal
    ).change(
        updateTotal
    ).find('input[type="number"]').each(function(){
        if('0' == $(this).attr('max')) $(this).attr('disabled', '');
    }).change(function(){
        var val    = nanCheck($(this).val(), 0);
        var maxVal = nanCheck($(this).attr('max'), 0);
        var minVal = nanCheck($(this).attr('min'), 0);
        if(val > maxVal) val = maxVal;
        if(val < minVal) val = minVal;
        $(this).val(val);
        var h = nanCheck($('#field-high-' + $(this).attr('name')).text(), 0);
        var t = val + h;
        $('#field-summary-' + $(this).attr('name')).text(t);
        uaForm.change();
    });
    $('button[us-target="add-field"]').click(function(){
        var addVal = nanCheck($(this).attr('us-data'), 0);
        var target = $('#' + $(this).attr('us-field'));
        var   nVal = addVal + nanCheck(target.val(), 0);
        target.val(nVal);
        target.change();
    });
});
