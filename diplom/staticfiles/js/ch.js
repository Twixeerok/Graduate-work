(function($) {
    $.fn.selectBox = function() {
      return this.each(function(){
        var $wrap = $(this);
        var $select = $wrap.find("select");
        var $label = $wrap.find("label");
        var $txt = $select.find("option:selected").text();
        var $disabled = $select.prop("disabled");
        
        if($disabled){
          $wrap.addClass("disabled");
        }
        
        $label.text($txt);
        
        $select.on("change", function(){
          $txt = $(this).find("option:selected").text();
          $label.text($txt);
        });
        
        $select.focusin(function(){
          $wrap.addClass("focus");
        }).focusout(function(){
          $wrap.removeClass("focus");
        });
        
      });
    }
   
  })(jQuery);
  
  $(function(){
    $(".box-select").selectBox();
  });