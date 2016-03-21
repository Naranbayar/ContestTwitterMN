$('.toolTip').tooltip()

var names = new Array();
	names[1] = "Улаанбаатар";
	names[2] = "Баянзүрх";
	names[3] = "Баянгол";
	names[4] = "Багануур";
	names[5] = "Багахангай";
	names[6] = "Налайх";
	names[7] = "Сүхбаатар";
	names[8] = "Хан-Уул";
	names[10] = "Сонгинохайрхан";
	names[12] = "Чингэлтэй";
	names[15] = "Архангай";
	names[18] = "Баян-Өлгий";
	names[24] = "Баянхонгор";
	names[26] = "Булган";
	names[28] = "Говь-Алтай";
	names[29] = "Говь-Сүмбэр";
	names[31] = "Дархан-Уул";
	names[33] = "Дорнод";
	names[36] = "Дорноговь";
	names[37] = "Дундговь";
	names[39] = "Завхан";
	names[40] = "Орхон";
	names[42] = "Өвөрхангай";
	names[44] = "Өмнөговь";
	names[48] = "Сүхбаатар";
	names[51] = "Сэлэнгэ";
	names[52] = "Төв-Аймаг";
	names[53] = "Увс";
	names[54] = "Ховд";
	names[55] = "Хөвсгөл";
	names[56] = "Хэнтий";
	
	$('path').mouseover(function() {
		if(this.id=="path-1"){
			$("g > path").css('fill', '#0b87e5');
		}else{
			$('#'+this.id).css('fill', '#0b87e5');
		}
		var str = this.id;
		var res = str.replace("path-","");
		$("#mapLabel").html(names[res]);
		
		$(this).mousemove(function(event) {
			$("#mapLabel").css({'left': event.pageX - 50 , 'top': event.pageY - 40 , 'display': 'block' });
		});
	
	});
	
	
		
	$('path').mouseout(function() {
	  	if(this.id=="path-1"){
			$("g > path").css('fill', '#00a8e9');
		}else{
			$('#'+this.id).css('fill', '#00a8e9');
		}
		$("#mapLabel").css('display', 'none');
		
	});
	
	$('path').click(function() {
		var str = this.id;
		var res = str.replace("path-","");
		// location.href="http://www.ulstor.mn/subcat/"+res+".html"; 
		location.href="javascript:;"; 
		self.focus(); 
	});
