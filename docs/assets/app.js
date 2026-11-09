
(function(){
  var toc=document.getElementById('toc');
  var filter=document.getElementById('tocFilter');
  var progress=document.getElementById('progress');
  var toTop=document.getElementById('toTop');
  var toggle=document.getElementById('menuToggle');
  var fab=document.getElementById('tocFab');
  var scrim=document.getElementById('scrim');
  var drawerClose=document.getElementById('drawerClose');
  var sidebar=document.getElementById('sidebar');
  var triggers=[toggle,fab].filter(Boolean);
  var mobile=window.matchMedia('(max-width:960px)');

  function setDrawer(open,returnFocus){
    if(!sidebar)return;
    sidebar.classList.toggle('open',open);
    if(scrim)scrim.classList.toggle('show',open);
    document.body.classList.toggle('nav-open',open&&mobile.matches);
    for(var i=0;i<triggers.length;i++)triggers[i].setAttribute('aria-expanded',open?'true':'false');
    if(!open&&returnFocus&&mobile.matches&&fab)fab.focus({preventScroll:true});
  }
  for(var t=0;t<triggers.length;t++){
    triggers[t].addEventListener('click',function(){
      setDrawer(!sidebar.classList.contains('open'),true);
    });
  }
  if(scrim)scrim.addEventListener('click',function(){setDrawer(false,true);});
  if(drawerClose)drawerClose.addEventListener('click',function(){setDrawer(false,true);});
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape')setDrawer(false,true);
  });
  if(toc)toc.addEventListener('click',function(e){
    if(e.target.closest('a'))setDrawer(false,false);
  });
  if(filter&&toc){
    filter.addEventListener('input',function(){
      var q=this.value.trim().toLowerCase();
      var items=toc.querySelectorAll('.toc-item');
      for(var i=0;i<items.length;i++){
        items[i].hidden=!!q&&(items[i].dataset.title||'').toLowerCase().indexOf(q)<0;
      }
      var groups=toc.querySelectorAll('.toc-group'),cur=null,has={};
      var all=toc.querySelectorAll('a');
      for(var j=0;j<all.length;j++){
        var el=all[j];
        if(el.classList.contains('toc-group')){cur=el;has[el.getAttribute('href')]=false;}
        else if(cur&&!el.hidden){has[cur.getAttribute('href')]=true;}
      }
      for(var k=0;k<groups.length;k++){
        groups[k].hidden=!!q&&!has[groups[k].getAttribute('href')];
      }
    });
    document.addEventListener('keydown',function(e){
      if((e.ctrlKey||e.metaKey)&&e.key==='k'){e.preventDefault();filter.focus();filter.select();}
    });
  }
  if(toTop)toTop.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});

  var heads=Array.prototype.slice.call(document.querySelectorAll('.prose h1[id],.prose h2[id]'));
  function update(){
    var d=document.documentElement;
    var max=d.scrollHeight-d.clientHeight;
    if(progress)progress.style.width=(max>0?(d.scrollTop/max*100):0)+'%';
    if(toTop)toTop.classList.toggle('show',d.scrollTop>420);
    if(!toc||!heads.length)return;
    var active=null;
    for(var i=0;i<heads.length;i++){
      if(heads[i].getBoundingClientRect().top<=110)active=heads[i].id;else break;
    }
    var links=toc.querySelectorAll('a');
    for(var j=0;j<links.length;j++){
      links[j].classList.toggle('active',!!active&&links[j].getAttribute('href')==='#'+active);
    }
  }
  window.addEventListener('scroll',update,{passive:true});
  window.addEventListener('resize',update);
  update();

  var tables=document.querySelectorAll('.prose table');
  for(var k=0;k<tables.length;k++){
    var table=tables[k];
    var wrap=document.createElement('div');
    wrap.className='table-wrap';
    table.parentNode.insertBefore(wrap,table);
    wrap.appendChild(table);
    var hint=document.createElement('span');
    hint.className='table-hint';
    hint.textContent='左右滑动查看完整表格 →';
    wrap.appendChild(hint);
  }
})();
