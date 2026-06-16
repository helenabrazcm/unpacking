<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Unpacking</title>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;800&family=Fraunces:ital,wght@0,700;1,400&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --ink:#1a1410;
  --paper:#f5ede0;
  --panel:#1c1510;
  --accent:#e8542a;
  --gold:#d4920a;
  --muted:#8a7a68;
}
html,body{width:100%;height:100%;overflow:hidden;background:#111}
body{font-family:'Nunito',sans-serif}
#app{width:100%;height:100%;display:flex;flex-direction:column}

/* HEADER */
#hdr{
  height:50px;background:#100c08;display:flex;align-items:center;
  padding:0 18px;gap:14px;border-bottom:1px solid rgba(255,255,255,0.06);flex-shrink:0;
}
#logo{font-family:'Fraunces',serif;font-size:22px;font-weight:700;color:var(--paper);letter-spacing:-.02em;font-style:italic}
#logo em{color:var(--gold);font-style:normal}
.pills{display:flex;gap:6px;flex:1;justify-content:center}
.pill{
  font-size:11px;font-weight:700;padding:5px 14px;border-radius:20px;
  border:1.5px solid rgba(255,255,255,0.12);background:transparent;
  color:rgba(255,255,255,0.4);cursor:pointer;transition:all .2s;
  letter-spacing:.05em;text-transform:uppercase;
}
.pill:hover{border-color:rgba(255,255,255,0.35);color:rgba(255,255,255,0.7)}
.pill.active{background:var(--gold);border-color:var(--gold);color:#1a1410}
.pill.locked{opacity:.22;pointer-events:none;cursor:default}
#score-wrap{text-align:right;min-width:88px}
#score-lbl{font-size:10px;color:rgba(255,255,255,0.3);letter-spacing:.08em;text-transform:uppercase}
#score-val{font-size:22px;font-weight:800;color:var(--gold)}

/* MAIN */
#main{flex:1;display:flex;overflow:hidden}

/* BOX PANEL */
#box-panel{
  width:196px;flex-shrink:0;background:#100c08;
  display:flex;flex-direction:column;
  border-right:1px solid rgba(255,255,255,0.05);
}
#box-hdr{padding:12px 12px 8px;border-bottom:1px solid rgba(255,255,255,0.05)}
#box-room{font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,0.3);margin-bottom:3px}
#box-title{font-size:15px;font-weight:800;color:var(--paper)}
#box-cnt{font-size:11px;color:var(--gold);margin-top:2px}
#box-list{flex:1;overflow-y:auto;padding:8px;display:flex;flex-direction:column;gap:4px}
#box-list::-webkit-scrollbar{width:3px}
#box-list::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.07);border-radius:2px}
.bitem{
  display:flex;align-items:center;gap:8px;padding:7px 9px;
  background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.07);
  border-radius:8px;cursor:grab;transition:background .15s,border-color .15s,transform .12s;
  user-select:none;
}
.bitem:hover{background:rgba(255,255,255,0.1);border-color:rgba(232,84,42,.5);transform:translateX(3px)}
.bitem:active{cursor:grabbing}
.bitem.faded{opacity:.25;pointer-events:none}
.bi-emoji{font-size:21px;flex-shrink:0;line-height:1}
.bi-info{flex:1;min-width:0}
.bi-name{font-size:12px;font-weight:700;color:var(--paper);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bi-sub{font-size:10px;color:rgba(255,255,255,0.28);margin-top:1px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bi-pts{font-size:10px;font-weight:800;color:var(--gold);flex-shrink:0}
#box-done{
  display:none;flex-direction:column;align-items:center;justify-content:center;
  flex:1;gap:8px;color:rgba(255,255,255,0.3);font-size:12px;text-align:center;padding:20px
}
#box-done.vis{display:flex}

/* ROOM */
#room{flex:1;position:relative;overflow:hidden}
#gc{position:absolute;inset:0;display:block}

/* RIGHT PANEL */
#right{
  width:182px;flex-shrink:0;background:#100c08;
  display:flex;flex-direction:column;padding:12px;gap:14px;
  border-left:1px solid rgba(255,255,255,0.05);overflow:hidden;
}
.rp-lbl{font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,0.28);margin-bottom:6px}
.prog-bar{height:5px;background:rgba(255,255,255,0.07);border-radius:3px;overflow:hidden;margin-bottom:4px}
.prog-fill{height:100%;background:linear-gradient(90deg,var(--accent),var(--gold));border-radius:3px;transition:width .5s}
.prog-txt{font-size:11px;color:rgba(255,255,255,0.35)}
.prog-txt b{color:var(--paper)}
.hint-box{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.07);border-radius:8px;padding:10px}
.hint-ttl{font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:4px}
.hint-msg{font-size:11px;color:rgba(255,255,255,0.5);line-height:1.55}
.log-sec{flex:1;overflow:hidden;display:flex;flex-direction:column}
#log{display:flex;flex-direction:column;gap:3px;overflow:hidden}
.lrow{
  display:flex;align-items:center;gap:6px;font-size:11px;color:rgba(255,255,255,0.4);
  padding:3px 6px;background:rgba(255,255,255,0.03);border-radius:4px;animation:lin .22s ease;
}
@keyframes lin{from{opacity:0;transform:translateY(-5px)}to{opacity:1;transform:none}}
.lrow .le{font-size:13px}
.lrow .ln{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow .lp{font-size:10px;font-weight:800;color:var(--gold);flex-shrink:0}
.lrow.perf .lp{color:#7de08a}

/* GHOST */
#ghost{position:fixed;pointer-events:none;z-index:9000;display:none;font-size:38px;transform:translate(-50%,-65%);filter:drop-shadow(0 4px 14px rgba(0,0,0,0.7))}

/* NOTIF */
#notif{
  position:fixed;top:60px;left:50%;transform:translateX(-50%) translateY(-10px);
  background:#1c1510;border:1px solid rgba(255,255,255,0.14);border-radius:30px;
  padding:7px 20px;font-size:13px;font-weight:700;color:var(--paper);
  pointer-events:none;z-index:9999;opacity:0;transition:opacity .22s,transform .22s;white-space:nowrap;
}
#notif.on{opacity:1;transform:translateX(-50%) translateY(0)}

/* TOOLTIP */
#tip{
  position:fixed;background:#1c1510;border:1px solid rgba(255,255,255,0.13);
  border-radius:8px;padding:8px 11px;font-size:11px;color:rgba(255,255,255,0.6);
  pointer-events:none;z-index:9999;display:none;max-width:150px;box-shadow:0 6px 20px rgba(0,0,0,0.5);
}
#tip .tn{font-weight:800;color:var(--paper);font-size:12px;margin-bottom:2px}
#tip .th{line-height:1.4}
#tip .tp{color:var(--gold);font-weight:700;margin-top:3px}

/* PARTICLE */
.particle{position:fixed;pointer-events:none;z-index:8000;font-size:17px;animation:pf .85s ease-out forwards}
@keyframes pf{0%{opacity:1;transform:translate(0,0) scale(1)}100%{opacity:0;transform:translate(var(--px),var(--py)) scale(.3)}}

/* VICTORY */
#victory{position:fixed;inset:0;background:rgba(16,10,4,.88);display:none;align-items:center;justify-content:center;z-index:10000;backdrop-filter:blur(8px)}
#victory.on{display:flex}
.vcard{background:var(--paper);border-radius:18px;padding:34px 42px;text-align:center;max-width:390px;width:90%;animation:vpop .4s cubic-bezier(.34,1.56,.64,1);color:var(--ink);box-shadow:0 24px 60px rgba(0,0,0,0.6)}
@keyframes vpop{from{opacity:0;transform:scale(.78)}to{opacity:1;transform:none}}
.vcard h2{font-family:'Fraunces',serif;font-size:27px;margin-bottom:4px}
.vcard .vsub{font-size:13px;color:var(--muted);margin-bottom:18px}
.vscore{font-family:'Fraunces',serif;font-size:54px;font-weight:700;color:var(--accent);line-height:1;margin-bottom:4px}
.vgrade{font-size:30px;margin-bottom:18px}
.vbd{background:rgba(0,0,0,0.06);border-radius:10px;padding:13px;font-size:12px;text-align:left;margin-bottom:18px}
.vrow{display:flex;justify-content:space-between;padding:3px 0}
.vrow .vk{color:var(--muted)}
.vrow .vv{font-weight:700}
.vrow.vbdr{border-top:1px solid rgba(0,0,0,0.1);margin-top:5px;padding-top:9px}
.vbtn{padding:11px 30px;background:var(--accent);color:#fff;border:none;border-radius:30px;font-family:'Nunito',sans-serif;font-size:14px;font-weight:800;cursor:pointer;transition:transform .15s,background .15s;box-shadow:0 4px 16px rgba(232,84,42,.35)}
.vbtn:hover{background:#c0401c;transform:scale(1.04)}
</style>
</head>
<body>
<div id="app">
  <div id="hdr">
    <div id="logo">Un<em>pack</em>ing</div>
    <div class="pills" id="pills"></div>
    <div id="score-wrap">
      <div id="score-lbl">pontos</div>
      <div id="score-val">0</div>
    </div>
  </div>
  <div id="main">
    <div id="box-panel">
      <div id="box-hdr">
        <div id="box-room">Caixa de Mudança</div>
        <div id="box-title">Quarto</div>
        <div id="box-cnt">0 itens</div>
      </div>
      <div id="box-list"></div>
      <div id="box-done"><span style="font-size:36px">🎉</span>Tudo organizado!</div>
    </div>
    <div id="room"><canvas id="gc"></canvas></div>
    <div id="right">
      <div>
        <div class="rp-lbl">Progresso</div>
        <div class="prog-bar"><div class="prog-fill" id="prog-fill" style="width:0%"></div></div>
        <div class="prog-txt"><b id="prog-pct">0%</b> organizado</div>
      </div>
      <div>
        <div class="rp-lbl">Dica</div>
        <div class="hint-box">
          <div class="hint-ttl" id="hint-ttl">Como jogar</div>
          <div class="hint-msg" id="hint-msg">Arraste os itens da caixa para os móveis. Cada item tem um lugar ideal!</div>
        </div>
      </div>
      <div class="log-sec">
        <div class="rp-lbl">Ações</div>
        <div id="log"></div>
      </div>
    </div>
  </div>
</div>

<div id="ghost"></div>
<div id="notif"></div>
<div id="tip"><div class="tn" id="tn"></div><div class="th" id="th"></div><div class="tp" id="tp"></div></div>

<div id="victory">
  <div class="vcard">
    <h2>🏠 Casa Organizada!</h2>
    <div class="vsub">Você terminou de desembalar tudo</div>
    <div class="vscore" id="v-score">0</div>
    <div class="vgrade" id="v-grade">⭐⭐⭐</div>
    <div class="vbd" id="v-bd"></div>
    <button class="vbtn" id="btn-restart">Jogar novamente</button>
  </div>
</div>

<script>
// ══════════════════════════════════════════════
//  CANVAS
// ══════════════════════════════════════════════
const canvas = document.getElementById('gc');
const ctx    = canvas.getContext('2d');

// ══════════════════════════════════════════════
//  DATA
// ══════════════════════════════════════════════
const ROOMS = [
{
  id:'bedroom', name:'Quarto',
  wall:'#5a7898', wallDark:'#3a5878', floor:'#c4a060', floorDark:'#a88040',
  trim:'#7a5830',
  zones:[
    {id:'bed',     label:'Cama',          rx:.04, ry:.28, rw:.36, rh:.54},
    {id:'desk',    label:'Escrivaninha',   rx:.50, ry:.18, rw:.44, rh:.24},
    {id:'shelf',   label:'Estante',        rx:.04, ry:.08, rw:.15, rh:.18},
    {id:'closet',  label:'Guarda-roupa',   rx:.75, ry:.44, rw:.20, rh:.46},
    {id:'floor',   label:'Chão',           rx:.05, ry:.84, rw:.40, rh:.10},
  ],
  items:[
    {id:'pillow',  e:'🛏️', n:'Travesseiro',    h:'Na cama',             bz:'bed',    bp:32, az:'shelf',  ap:10},
    {id:'bear',    e:'🧸', n:'Ursinho',         h:'Na cama ou estante',  bz:'bed',    bp:28, az:'shelf',  ap:22},
    {id:'blanket', e:'🛌', n:'Cobertor',        h:'Na cama',             bz:'bed',    bp:30, az:'floor',  ap:4},
    {id:'book',    e:'📖', n:'Livro',           h:'Na estante',          bz:'shelf',  bp:34, az:'desk',   ap:20},
    {id:'novels',  e:'📚', n:'Romances',        h:'Na estante',          bz:'shelf',  bp:34, az:'bed',    ap:12},
    {id:'laptop',  e:'💻', n:'Notebook',        h:'Na escrivaninha',     bz:'desk',   bp:38, az:'floor',  ap:4},
    {id:'lamp',    e:'🪔', n:'Luminária',       h:'Na escrivaninha',     bz:'desk',   bp:30, az:'shelf',  ap:16},
    {id:'clock',   e:'⏰', n:'Despertador',     h:'Na escrivaninha',     bz:'desk',   bp:30, az:'bed',    ap:22},
    {id:'phone',   e:'📱', n:'Celular',         h:'Na escrivaninha',     bz:'desk',   bp:28, az:'bed',    ap:18},
    {id:'clothes', e:'👕', n:'Camisetas',       h:'No guarda-roupa',     bz:'closet', bp:36, az:'floor',  ap:2},
    {id:'shoes',   e:'👟', n:'Tênis',           h:'No chão',             bz:'floor',  bp:20, az:'closet', ap:14},
    {id:'photo',   e:'🖼️', n:'Foto',            h:'Na estante',          bz:'shelf',  bp:32, az:'desk',   ap:18},
    {id:'plant',   e:'🪴', n:'Planta',          h:'Na janela/escrivaninha', bz:'desk', bp:26, az:'floor', ap:20},
    {id:'hdp',     e:'🎧', n:'Fone de ouvido',  h:'Na escrivaninha',     bz:'desk',   bp:28, az:'shelf',  ap:20},
  ]
},
{
  id:'kitchen', name:'Cozinha',
  wall:'#7aaa68', wallDark:'#4a7a3a', floor:'#d4c48a', floorDark:'#b0a060',
  trim:'#7a6030',
  zones:[
    {id:'counter', label:'Bancada',   rx:.04, ry:.10, rw:.54, rh:.28},
    {id:'fridge',  label:'Geladeira', rx:.04, ry:.44, rw:.18, rh:.46},
    {id:'cabinet', label:'Armário',   rx:.65, ry:.08, rw:.30, rh:.54},
    {id:'floor',   label:'Chão',      rx:.26, ry:.65, rw:.44, rh:.24},
  ],
  items:[
    {id:'pan',    e:'🍳', n:'Frigideira',  h:'Na bancada',       bz:'counter', bp:30, az:'cabinet', ap:20},
    {id:'pot',    e:'🫕', n:'Panela',      h:'No armário',       bz:'cabinet', bp:30, az:'counter', ap:22},
    {id:'mug',    e:'☕', n:'Caneca',      h:'No armário',       bz:'cabinet', bp:26, az:'counter', ap:18},
    {id:'knife',  e:'🔪', n:'Facas',       h:'Na bancada',       bz:'counter', bp:28, az:'floor',   ap:4},
    {id:'fruit',  e:'🍎', n:'Fruteira',    h:'Na bancada',       bz:'counter', bp:22, az:'floor',   ap:10},
    {id:'kettle', e:'🫖', n:'Chaleira',    h:'Na bancada',       bz:'counter', bp:28, az:'cabinet', ap:10},
    {id:'plate',  e:'🍽️', n:'Pratos',      h:'No armário',       bz:'cabinet', bp:26, az:'counter', ap:16},
    {id:'spice',  e:'🧂', n:'Temperos',    h:'Na bancada',       bz:'counter', bp:22, az:'cabinet', ap:18},
    {id:'wine',   e:'🍷', n:'Vinho',       h:'Na geladeira',     bz:'fridge',  bp:30, az:'cabinet', ap:14},
    {id:'bread',  e:'🍞', n:'Pão',         h:'Na bancada',       bz:'counter', bp:20, az:'floor',   ap:8},
    {id:'blndr',  e:'🥤', n:'Liquidificador', h:'Na bancada',   bz:'counter', bp:26, az:'cabinet', ap:12},
  ]
},
{
  id:'office', name:'Escritório',
  wall:'#7878b0', wallDark:'#505088', floor:'#b4a488', floorDark:'#908060',
  trim:'#6a5840',
  zones:[
    {id:'desk',  label:'Mesa de trabalho', rx:.08, ry:.14, rw:.60, rh:.28},
    {id:'shelf', label:'Estante',          rx:.74, ry:.06, rw:.20, rh:.82},
    {id:'couch', label:'Sofá',             rx:.06, ry:.62, rw:.52, rh:.28},
    {id:'floor', label:'Chão',             rx:.08, ry:.50, rw:.40, rh:.10},
  ],
  items:[
    {id:'monitor', e:'🖥️', n:'Monitor',    h:'Na mesa',        bz:'desk',  bp:40, az:'floor', ap:4},
    {id:'kbd',     e:'⌨️', n:'Teclado',    h:'Na mesa',        bz:'desk',  bp:36, az:'floor', ap:4},
    {id:'mouse2',  e:'🖱️', n:'Mouse',      h:'Na mesa',        bz:'desk',  bp:34, az:'floor', ap:4},
    {id:'notepad', e:'📓', n:'Caderno',    h:'Na mesa',        bz:'desk',  bp:28, az:'shelf', ap:22},
    {id:'files',   e:'📁', n:'Pastas',     h:'Na estante',     bz:'shelf', bp:32, az:'desk',  ap:20},
    {id:'trophy',  e:'🏆', n:'Troféu',     h:'Na estante',     bz:'shelf', bp:38, az:'desk',  ap:14},
    {id:'cactus',  e:'🌵', n:'Cacto',      h:'Na mesa',        bz:'desk',  bp:26, az:'floor', ap:20},
    {id:'coffee',  e:'☕', n:'Café',       h:'Na mesa',        bz:'desk',  bp:22, az:'floor', ap:8},
    {id:'hset',    e:'🎧', n:'Headset',    h:'Na mesa/estante',bz:'desk',  bp:28, az:'shelf', ap:20},
    {id:'camera',  e:'📷', n:'Câmera',     h:'Na estante',     bz:'shelf', bp:32, az:'desk',  ap:24},
    {id:'printer', e:'🖨️', n:'Impressora', h:'Na mesa',        bz:'desk',  bp:36, az:'floor', ap:4},
    {id:'lamp2',   e:'💡', n:'Luminária',  h:'Na mesa',        bz:'desk',  bp:28, az:'shelf', ap:14},
  ]
}
];

// ══════════════════════════════════════════════
//  STATE
// ══════════════════════════════════════════════
let G = {curRoom:0,rooms:[],score:0,placed:0,total:0,startTime:0};

function initGame(){
  G.score=0; G.placed=0; G.startTime=Date.now();
  G.rooms = ROOMS.map((rd,i)=>({
    def:rd,
    box:[...rd.items.map(it=>({...it}))],
    placed:{},
    score:0,
    unlocked:i===0,
  }));
  G.total = ROOMS.reduce((s,r)=>s+r.items.length,0);
  G.curRoom=0;
  document.getElementById('log').innerHTML='';
}

function calcScore(item,zone){
  if(zone===item.bz) return item.bp;
  if(zone===item.az) return item.ap;
  return Math.max(2,Math.floor(item.bp*0.07));
}

function placeItem(ri,item,zone){
  const room=G.rooms[ri];
  const pts=calcScore(item,zone);
  const perfect=zone===item.bz, good=zone===item.az;
  room.placed[item.id]={...item,zone,pts};
  room.box=room.box.filter(i=>i.id!==item.id);
  room.score+=pts; G.score+=pts; G.placed++;
  addLog(item.e,item.n,pts,perfect);
  setHint(perfect?'✨ Lugar perfeito!':good?'👍 Bom lugar!':'📦 Colocado',
    perfect?`${item.n} está no lugar ideal!`:good?`Bom lugar! Ideal: ${item.h}.`:`Dica: ${item.h}`);
  checkUnlock(); refreshBox(ri); updateUI(); redraw();
  spawnParticles(zone,ri,perfect);
  notify(perfect?`✨ Perfeito! +${pts}`:good?`👍 Bom lugar! +${pts}`:`+${pts} pts`);
  checkVictory();
}

function removeItem(ri,iid){
  const room=G.rooms[ri], p=room.placed[iid];
  if(!p) return null;
  room.score-=p.pts; G.score-=p.pts; G.placed--;
  delete room.placed[iid];
  const def=room.def.items.find(i=>i.id===iid);
  room.box.push({...def});
  refreshBox(ri); updateUI();
  return {...def};
}

function checkUnlock(){
  G.rooms.forEach((r,i)=>{
    if(i===0) return;
    const prev=G.rooms[i-1];
    if(!r.unlocked && Object.keys(prev.placed).length>=Math.ceil(prev.def.items.length*0.5)){
      r.unlocked=true; notify(`🔓 ${r.def.name} desbloqueado!`); renderPills();
    }
  });
}

function checkVictory(){if(G.placed>=G.total) setTimeout(showVictory,700);}
function showVictory(){
  const maxPts=ROOMS.reduce((s,r)=>s+r.items.reduce((ss,i)=>ss+i.bp,0),0);
  const pct=Math.round(G.score/maxPts*100);
  const grade=pct>=90?'⭐⭐⭐':pct>=70?'⭐⭐':pct>=45?'⭐':'💔';
  const el=Math.round((Date.now()-G.startTime)/1000);
  const m=Math.floor(el/60),s=el%60;
  document.getElementById('v-score').textContent=G.score+' pts';
  document.getElementById('v-grade').textContent=grade;
  let bd=''; G.rooms.forEach(r=>{bd+=`<div class="vrow"><span class="vk">${r.def.name}</span><span class="vv">${r.score} pts</span></div>`;});
  bd+=`<div class="vrow vbdr"><span class="vk">Precisão</span><span class="vv">${pct}%</span></div>`;
  bd+=`<div class="vrow"><span class="vk">Tempo</span><span class="vv">${m}:${String(s).padStart(2,'0')}</span></div>`;
  document.getElementById('v-bd').innerHTML=bd;
  document.getElementById('victory').classList.add('on');
}

// ══════════════════════════════════════════════
//  DRAW ENGINE
// ══════════════════════════════════════════════
function W(){return canvas.width;}
function H(){return canvas.height;}
function zr(z){ // zone rect in pixels
  const room=G.rooms[G.curRoom];
  const zd=room.def.zones.find(zz=>zz.id===z);
  if(!zd) return null;
  return {x:zd.rx*W(),y:zd.ry*H(),w:zd.rw*W(),h:zd.rh*H()};
}

function resize(){
  const el=document.getElementById('room');
  canvas.width=el.clientWidth; canvas.height=el.clientHeight;
  redraw();
}
new ResizeObserver(resize).observe(document.getElementById('room'));

function redraw(){
  if(!canvas.width||!canvas.height) return;
  ctx.clearRect(0,0,W(),H());
  const room=G.rooms[G.curRoom], rd=room.def;

  drawRoomBg(rd);

  // Draw furniture for this room
  (DRAW_FURN[rd.id]||[]).forEach(f=>{
    const r=zr(f.id);
    if(r) f.fn(r, room);
  });

  // Draw placed items
  Object.values(room.placed).forEach(item=>drawPlacedItem(room,item));

  // Drop zone highlight
  if(drag.active&&drag.overZone){
    const r=zr(drag.overZone);
    if(r){
      ctx.save();
      ctx.strokeStyle='rgba(212,146,10,.85)';
      ctx.lineWidth=3; ctx.setLineDash([7,4]);
      ctx.strokeRect(r.x+2,r.y+2,r.w-4,r.h-4);
      ctx.fillStyle='rgba(212,146,10,.1)';
      ctx.fillRect(r.x+2,r.y+2,r.w-4,r.h-4);
      ctx.restore();
    }
  }
}

// ── ROOM BACKGROUND ──────────────────────────────────────
function drawRoomBg(rd){
  // Wall gradient
  const wg=ctx.createLinearGradient(0,0,0,H()*0.6);
  wg.addColorStop(0,rd.wallDark); wg.addColorStop(1,rd.wall);
  ctx.fillStyle=wg; ctx.fillRect(0,0,W(),H()*0.6);

  // Subtle wall texture
  ctx.save(); ctx.globalAlpha=0.04;
  for(let y=0;y<H()*0.6;y+=32){
    ctx.fillStyle='#000'; ctx.fillRect(0,y,W(),1);
  }
  ctx.restore();

  // Floor
  const fg=ctx.createLinearGradient(0,H()*0.56,0,H());
  fg.addColorStop(0,rd.floorDark); fg.addColorStop(1,rd.floor);
  ctx.fillStyle=fg; ctx.fillRect(0,H()*0.56,W(),H()*0.44);

  // Floor planks
  ctx.save(); ctx.globalAlpha=0.09;
  const ph=20,pw=72;
  for(let row=0;row<Math.ceil(H()*0.44/ph)+1;row++){
    for(let col=0;col<Math.ceil(W()/pw)+1;col++){
      const ox=(row%2)*pw*0.5;
      ctx.strokeStyle='#000'; ctx.lineWidth=0.7;
      ctx.strokeRect(col*pw-ox, H()*0.56+row*ph, pw, ph);
    }
  }
  ctx.restore();

  // Skirting board
  ctx.fillStyle=rd.trim||'#7a5830';
  ctx.fillRect(0,H()*0.56-5,W(),10);
  ctx.fillStyle='rgba(0,0,0,0.3)'; ctx.fillRect(0,H()*0.56-5,W(),1.5);
  ctx.fillStyle='rgba(255,255,255,0.1)'; ctx.fillRect(0,H()*0.56+3,W(),1.5);

  // Shadow at base
  const sg=ctx.createLinearGradient(0,H()*0.56,0,H()*0.56+70);
  sg.addColorStop(0,'rgba(0,0,0,.22)'); sg.addColorStop(1,'transparent');
  ctx.fillStyle=sg; ctx.fillRect(0,H()*0.56,W(),70);

  // Ceiling
  ctx.fillStyle='rgba(255,255,255,0.05)';
  ctx.fillRect(0,0,W(),6);

  // Window
  drawWindow(W()*0.33, H()*0.06, W()*0.28, H()*0.36);
  // Door (right)
  drawDoor(W()*0.80, H()*0.18, W()*0.13, H()*0.38);
}

function rrect(x,y,w,h,r,fill,stroke){
  ctx.beginPath();
  ctx.moveTo(x+r,y); ctx.lineTo(x+w-r,y); ctx.quadraticCurveTo(x+w,y,x+w,y+r);
  ctx.lineTo(x+w,y+h-r); ctx.quadraticCurveTo(x+w,y+h,x+w-r,y+h);
  ctx.lineTo(x+r,y+h); ctx.quadraticCurveTo(x,y+h,x,y+h-r);
  ctx.lineTo(x,y+r); ctx.quadraticCurveTo(x,y,x+r,y);
  ctx.closePath();
  if(fill){ctx.fillStyle=fill;ctx.fill();}
  if(stroke){ctx.strokeStyle=stroke;ctx.stroke();}
}

function drawWindow(wx,wy,ww,wh){
  ctx.save();
  // Outer frame
  rrect(wx-10,wy-10,ww+20,wh+14,4,'#a08060');
  // Sky
  const sk=ctx.createLinearGradient(wx,wy,wx,wy+wh);
  sk.addColorStop(0,'#7ab0d8'); sk.addColorStop(1,'#c8e4f4');
  rrect(wx,wy,ww,wh,2,null); ctx.fillStyle=sk; ctx.fill();
  // Clouds
  ctx.fillStyle='rgba(255,255,255,0.85)';
  [[.25,.28,.12],[.55,.22,.09],[.65,.3,.07]].forEach(([rx,ry,rr])=>{
    ctx.beginPath(); ctx.arc(wx+ww*rx,wy+wh*ry,ww*rr,0,Math.PI*2); ctx.fill();
  });
  // Cross
  ctx.strokeStyle='rgba(160,190,210,0.7)'; ctx.lineWidth=3;
  ctx.beginPath(); ctx.moveTo(wx+ww/2,wy); ctx.lineTo(wx+ww/2,wy+wh); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(wx,wy+wh/2); ctx.lineTo(wx+ww,wy+wh/2); ctx.stroke();
  // Glow
  ctx.fillStyle='rgba(255,255,255,0.06)';
  ctx.fillRect(wx,wy,ww*0.48,wh);
  // Curtains
  const cg1=ctx.createLinearGradient(wx-12,0,wx+10,0);
  cg1.addColorStop(0,'#d8c4a0'); cg1.addColorStop(1,'rgba(216,196,160,0)');
  ctx.fillStyle=cg1; ctx.fillRect(wx-12,wy-12,22,wh+18);
  const cg2=ctx.createLinearGradient(wx+ww-10,0,wx+ww+12,0);
  cg2.addColorStop(0,'rgba(216,196,160,0)'); cg2.addColorStop(1,'#d8c4a0');
  ctx.fillStyle=cg2; ctx.fillRect(wx+ww-10,wy-12,22,wh+18);
  // Curtain rod
  ctx.fillStyle='#a08050'; ctx.fillRect(wx-14,wy-14,ww+28,6);
  ctx.restore();
}

function drawDoor(dx,dy,dw,dh){
  ctx.save();
  rrect(dx-7,dy-7,dw+14,dh+8,3,'#8a6840');
  rrect(dx,dy,dw,dh,2,'#c09a60');
  ctx.strokeStyle='rgba(0,0,0,0.15)'; ctx.lineWidth=1.2;
  ctx.strokeRect(dx+8,dy+10,dw-16,dh*.44-6);
  ctx.strokeRect(dx+8,dy+dh*.5,dw-16,dh*.44);
  ctx.fillStyle='#d4a840';
  ctx.beginPath(); ctx.arc(dx+12,dy+dh*.5,5,0,Math.PI*2); ctx.fill();
  ctx.restore();
}

// ── FURNITURE DRAWERS ──────────────────────────────────────
const DRAW_FURN = {
  bedroom:[
    {id:'bed',     fn:drawBed},
    {id:'desk',    fn:drawDesk},
    {id:'shelf',   fn:drawShelf},
    {id:'closet',  fn:drawCloset},
  ],
  kitchen:[
    {id:'counter', fn:drawCounter},
    {id:'fridge',  fn:drawFridge},
    {id:'cabinet', fn:drawCabinet},
  ],
  office:[
    {id:'desk',    fn:drawBigDesk},
    {id:'shelf',   fn:drawBookcase},
    {id:'couch',   fn:drawCouch},
  ]
};

function shadow(r,h=18){
  ctx.save();
  const sg=ctx.createLinearGradient(r.x,r.y+r.h,r.x,r.y+r.h+h);
  sg.addColorStop(0,'rgba(0,0,0,.2)'); sg.addColorStop(1,'transparent');
  ctx.fillStyle=sg; ctx.fillRect(r.x+4,r.y+r.h,r.w-8,h);
  ctx.restore();
}

function drawBed(r){
  ctx.save();
  // Frame
  rrect(r.x,r.y,r.w,r.h,8,'#4a3860');
  // Headboard
  rrect(r.x,r.y,r.w,r.h*.18,7,'#6a4a88');
  // Mattress
  rrect(r.x+8,r.y+r.h*.18,r.w-16,r.h*.78,6,'#ede4d4');
  // Pillow
  rrect(r.x+14,r.y+r.h*.22,r.w-28,r.h*.18,5,'#f8f2ea','rgba(0,0,0,.08)');
  ctx.strokeStyle='rgba(0,0,0,.07)'; ctx.lineWidth=1; ctx.stroke();
  // Blanket
  rrect(r.x+8,r.y+r.h*.42,r.w-16,r.h*.52,5,'#7880c8');
  rrect(r.x+8,r.y+r.h*.42,r.w-16,r.h*.09,5,'rgba(255,255,255,.15)');
  // Highlight on headboard
  ctx.fillStyle='rgba(255,255,255,.07)';
  rrect(r.x+6,r.y+4,r.w-12,r.h*.1,4,null); ctx.fill();
  ctx.restore(); shadow(r);
}

function drawDesk(r){
  ctx.save();
  // Legs first (behind top)
  ctx.fillStyle='#5a4030';
  const lw=10, lh=r.h*.78;
  ctx.fillRect(r.x+8,r.y+r.h*.22,lw,lh);
  ctx.fillRect(r.x+r.w-lw-8,r.y+r.h*.22,lw,lh);
  // Desk top
  rrect(r.x,r.y,r.w,r.h*.24,4,'#7a5c44');
  rrect(r.x+2,r.y+2,r.w-4,r.h*.24-4,3,'rgba(255,255,255,.07)');
  // Drawer
  rrect(r.x+r.w*.28,r.y+r.h*.07,r.w*.44,r.h*.12,3,'#9a7858','rgba(0,0,0,.2)');
  ctx.strokeStyle='rgba(0,0,0,.2)'; ctx.lineWidth=.5; ctx.stroke();
  ctx.fillStyle='rgba(255,200,80,.5)';
  ctx.beginPath(); ctx.arc(r.x+r.w*.5,r.y+r.h*.14,2.5,0,Math.PI*2); ctx.fill();
  ctx.restore(); shadow(r);
}

function drawShelf(r){
  ctx.save();
  // Back
  ctx.fillStyle='#7a5830'; ctx.fillRect(r.x,r.y,r.w,r.h);
  // Shelves
  const ns=4;
  for(let i=0;i<=ns;i++){
    const sy=r.y+r.h*i/ns;
    rrect(r.x-2,sy,r.w+4,6,1,'#9a7040');
    ctx.fillStyle='rgba(255,255,255,.08)'; ctx.fillRect(r.x-2,sy,r.w+4,2);
  }
  // Sides
  ctx.fillStyle='#6a4820'; ctx.fillRect(r.x,r.y,5,r.h); ctx.fillRect(r.x+r.w-5,r.y,5,r.h);
  // Books on shelves
  const bc=['#c04444','#4a8844','#4468c4','#c49020','#8844c0'];
  for(let s=0;s<ns;s++){
    const sy=r.y+r.h*s/ns+6;
    const sh=r.h/ns-7;
    let bx=r.x+7;
    for(let b=0;b<6;b++){
      const bw=5+Math.random()*4;
      ctx.fillStyle=bc[(s*3+b)%bc.length]; ctx.fillRect(bx,sy+2,bw,sh-3);
      ctx.fillStyle='rgba(0,0,0,.15)'; ctx.fillRect(bx+bw-1,sy+2,1,sh-3);
      bx+=bw+1; if(bx>r.x+r.w-8) break;
    }
  }
  ctx.restore(); shadow(r);
}

function drawCloset(r){
  ctx.save();
  // Body
  rrect(r.x,r.y,r.w,r.h,4,'#5a4430');
  // Door divider
  ctx.strokeStyle='rgba(0,0,0,.35)'; ctx.lineWidth=2;
  ctx.beginPath(); ctx.moveTo(r.x+r.w/2,r.y); ctx.lineTo(r.x+r.w/2,r.y+r.h); ctx.stroke();
  // Panels
  ctx.strokeStyle='rgba(0,0,0,.12)'; ctx.lineWidth=.8;
  ctx.strokeRect(r.x+8,r.y+10,r.w/2-14,r.h*.44);
  ctx.strokeRect(r.x+8,r.y+r.h*.5,r.w/2-14,r.h*.44);
  ctx.strokeRect(r.x+r.w/2+6,r.y+10,r.w/2-14,r.h*.44);
  ctx.strokeRect(r.x+r.w/2+6,r.y+r.h*.5,r.w/2-14,r.h*.44);
  // Handles
  ctx.fillStyle='rgba(220,180,70,.7)';
  ctx.beginPath(); ctx.arc(r.x+r.w/2-9,r.y+r.h*.5,3.5,0,Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(r.x+r.w/2+9,r.y+r.h*.5,3.5,0,Math.PI*2); ctx.fill();
  // Top
  rrect(r.x,r.y,r.w,8,4,'#4a3420');
  ctx.restore(); shadow(r);
}

function drawCounter(r){
  ctx.save();
  // Backsplash / tiles on wall behind
  ctx.fillStyle='#d8c898'; ctx.fillRect(r.x,r.y,r.w,r.h*.3);
  ctx.strokeStyle='rgba(0,0,0,.08)'; ctx.lineWidth=.5;
  for(let tx=r.x;tx<r.x+r.w;tx+=24){ctx.beginPath();ctx.moveTo(tx,r.y);ctx.lineTo(tx,r.y+r.h*.3);ctx.stroke();}
  for(let ty=r.y;ty<r.y+r.h*.3;ty+=18){ctx.beginPath();ctx.moveTo(r.x,ty);ctx.lineTo(r.x+r.w,ty);ctx.stroke();}
  // Base cabinets
  ctx.fillStyle='#b89860'; ctx.fillRect(r.x,r.y+r.h*.35,r.w,r.h*.65);
  // Cabinet doors
  const dw=r.w/3;
  for(let i=0;i<3;i++){
    ctx.strokeStyle='rgba(0,0,0,.15)'; ctx.lineWidth=1;
    ctx.strokeRect(r.x+i*dw+5,r.y+r.h*.42,dw-10,r.h*.52);
    ctx.fillStyle='rgba(255,200,70,.45)';
    ctx.beginPath(); ctx.arc(r.x+i*dw+dw/2,r.y+r.h*.69,3,0,Math.PI*2); ctx.fill();
  }
  // Counter top
  rrect(r.x-3,r.y+r.h*.28,r.w+6,r.h*.14,2,'#e0c88a');
  // Sink
  rrect(r.x+r.w*.1,r.y+r.h*.3,r.w*.26,r.h*.1,3,'rgba(200,220,240,.55)','rgba(0,0,0,.2)');
  // Faucet
  ctx.fillStyle='#b8b8b8'; ctx.fillRect(r.x+r.w*.22,r.y+r.h*.18,4,r.h*.14);
  ctx.restore(); shadow(r);
}

function drawFridge(r){
  ctx.save();
  const fg=ctx.createLinearGradient(r.x,r.y,r.x+r.w,r.y);
  fg.addColorStop(0,'#dce8f2'); fg.addColorStop(1,'#c4d8e4');
  rrect(r.x,r.y,r.w,r.h,6,null); ctx.fillStyle=fg; ctx.fill();
  ctx.strokeStyle='rgba(100,140,180,.3)'; ctx.lineWidth=1; ctx.stroke();
  // Divider
  ctx.strokeStyle='rgba(0,0,0,.2)'; ctx.lineWidth=1;
  ctx.beginPath(); ctx.moveTo(r.x+5,r.y+r.h*.32); ctx.lineTo(r.x+r.w-5,r.y+r.h*.32); ctx.stroke();
  // Handles
  ctx.fillStyle='#90a8b8';
  ctx.fillRect(r.x+r.w*.18,r.y+r.h*.09,r.w*.6,5);
  ctx.fillRect(r.x+r.w*.18,r.y+r.h*.46,r.w*.6,5);
  // Seals
  ctx.strokeStyle='rgba(0,0,0,.07)'; ctx.lineWidth=.7;
  ctx.strokeRect(r.x+5,r.y+5,r.w-10,r.h*.26);
  ctx.strokeRect(r.x+5,r.y+r.h*.33,r.w-10,r.h*.62);
  // Highlight
  ctx.fillStyle='rgba(255,255,255,.12)';
  ctx.fillRect(r.x+5,r.y+5,r.w*.35,r.h*.94);
  ctx.restore(); shadow(r);
}

function drawCabinet(r){
  ctx.save();
  rrect(r.x,r.y,r.w,r.h,4,'#9a7450');
  ctx.strokeStyle='rgba(0,0,0,.25)'; ctx.lineWidth=1.5;
  ctx.beginPath(); ctx.moveTo(r.x+r.w/2,r.y); ctx.lineTo(r.x+r.w/2,r.y+r.h); ctx.stroke();
  ctx.strokeStyle='rgba(0,0,0,.1)'; ctx.lineWidth=.7;
  ctx.strokeRect(r.x+7,r.y+8,r.w/2-13,r.h/2-12);
  ctx.strokeRect(r.x+7,r.y+r.h/2+4,r.w/2-13,r.h/2-12);
  ctx.strokeRect(r.x+r.w/2+6,r.y+8,r.w/2-13,r.h/2-12);
  ctx.strokeRect(r.x+r.w/2+6,r.y+r.h/2+4,r.w/2-13,r.h/2-12);
  ctx.fillStyle='rgba(220,180,60,.7)';
  ctx.beginPath(); ctx.arc(r.x+r.w/2-9,r.y+r.h*.5,3.5,0,Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(r.x+r.w/2+9,r.y+r.h*.5,3.5,0,Math.PI*2); ctx.fill();
  rrect(r.x,r.y,r.w,7,4,'#7a5430');
  rrect(r.x,r.y+r.h-7,r.w,7,4,'#7a5430');
  ctx.restore(); shadow(r);
}

function drawBigDesk(r){
  ctx.save();
  // Legs
  ctx.fillStyle='#2a1c10';
  ctx.fillRect(r.x+10,r.y+r.h*.22,12,r.h*.78);
  ctx.fillRect(r.x+r.w-22,r.y+r.h*.22,12,r.h*.78);
  // Drawer pedestal
  ctx.fillStyle='#3a2416'; ctx.fillRect(r.x+r.w-60,r.y+r.h*.22,50,r.h*.65);
  for(let i=0;i<3;i++){
    rrect(r.x+r.w-56,r.y+r.h*.26+i*r.h*.18,42,r.h*.14,2,'rgba(255,255,255,.05)','rgba(0,0,0,.35)');
    ctx.lineWidth=.5; ctx.stroke();
    ctx.fillStyle='rgba(220,170,60,.45)';
    ctx.beginPath(); ctx.arc(r.x+r.w-35,r.y+r.h*.34+i*r.h*.18,2.5,0,Math.PI*2); ctx.fill();
  }
  // Top
  rrect(r.x,r.y,r.w,r.h*.24,4,'#3c2818');
  rrect(r.x+2,r.y+2,r.w-4,r.h*.24-4,3,'rgba(255,255,255,.06)');
  ctx.restore(); shadow(r);
}

function drawBookcase(r){
  ctx.save();
  ctx.fillStyle='#4a3020'; ctx.fillRect(r.x,r.y,r.w,r.h);
  const ns=6;
  for(let i=0;i<=ns;i++){
    const sy=r.y+r.h*i/ns;
    rrect(r.x,sy,r.w,5,1,'#6a4830');
    ctx.fillStyle='rgba(255,255,255,.07)'; ctx.fillRect(r.x,sy,r.w,2);
  }
  ctx.fillStyle='#3a2010'; ctx.fillRect(r.x,r.y,5,r.h); ctx.fillRect(r.x+r.w-5,r.y,5,r.h);
  const bc=['#c04444','#4a8844','#4468c4','#c09020','#8844c0','#44808c'];
  for(let s=0;s<ns;s++){
    const sy=r.y+r.h*s/ns+5;
    const sh=r.h/ns-6;
    let bx=r.x+7;
    for(let b=0;b<Math.floor(r.w/9);b++){
      const bw=6+Math.random()*4;
      ctx.fillStyle=bc[(s*4+b)%bc.length]; ctx.fillRect(bx,sy+2,bw,sh-3);
      ctx.fillStyle='rgba(0,0,0,.12)'; ctx.fillRect(bx+bw-1,sy+2,1,sh-3);
      bx+=bw+1; if(bx>r.x+r.w-8) break;
    }
  }
  ctx.restore(); shadow(r);
}

function drawCouch(r){
  ctx.save();
  // Back
  rrect(r.x,r.y,r.w,r.h*.38,6,'#503870');
  // Arms
  rrect(r.x,r.y+r.h*.34,12,r.h*.52,3,'#403060');
  rrect(r.x+r.w-12,r.y+r.h*.34,12,r.h*.52,3,'#403060');
  // Seat
  rrect(r.x+10,r.y+r.h*.34,r.w-20,r.h*.46,5,'#6050a0');
  // Cushions
  const nc=3, cw=(r.w-20)/nc-5;
  for(let i=0;i<nc;i++){
    rrect(r.x+14+i*(cw+5),r.y+r.h*.36,cw,r.h*.41,4,'#7060b0');
    ctx.fillStyle='rgba(255,255,255,.08)';
    rrect(r.x+16+i*(cw+5),r.y+r.h*.37,cw-4,r.h*.1,3,null); ctx.fill();
  }
  // Legs
  ctx.fillStyle='#302040';
  for(let i=0;i<4;i++) ctx.fillRect(r.x+16+i*(r.w-32)/3,r.y+r.h*.84,9,r.h*.16);
  ctx.restore(); shadow(r);
}

// ── DRAW PLACED ITEM ─────────────────────────────────────
function drawPlacedItem(room,item){
  const r=zr(item.zone);
  if(!r) return;
  const all=Object.values(room.placed).filter(i=>i.zone===item.zone);
  const idx=all.findIndex(i=>i.id===item.id);
  const n=all.length;
  const cols=Math.min(n,Math.max(1,Math.round(Math.sqrt(n*r.w/r.h))));
  const rows=Math.ceil(n/cols);
  const cw=r.w/cols, ch=r.h/rows;
  const col=idx%cols, row=Math.floor(idx/cols);
  const cx=r.x+col*cw+cw/2, cy=r.y+row*ch+ch/2;
  const size=Math.min(cw,ch)*0.72;

  ctx.save();
  // Subtle glow bg
  ctx.fillStyle='rgba(255,255,255,.13)';
  ctx.beginPath(); ctx.arc(cx,cy,size*.44,0,Math.PI*2); ctx.fill();

  ctx.font=`${size*.5}px "Segoe UI Emoji","Apple Color Emoji",sans-serif`;
  ctx.textAlign='center'; ctx.textBaseline='middle';
  ctx.fillText(item.e,cx,cy);
  ctx.restore();
}

// ══════════════════════════════════════════════
//  DRAG & DROP
// ══════════════════════════════════════════════
const drag={active:false,item:null,fromBox:false,overZone:null};
const ghost=document.getElementById('ghost');

function startDrag(e,item,fromBox){
  e.preventDefault();
  drag.active=true; drag.item=item; drag.fromBox=fromBox; drag.overZone=null;
  ghost.textContent=item.e; ghost.style.display='block';
  const cx=e.touches?e.touches[0].clientX:e.clientX;
  const cy=e.touches?e.touches[0].clientY:e.clientY;
  moveGhost(cx,cy);
  if(fromBox) document.querySelectorAll(`.bitem[data-id="${item.id}"]`).forEach(el=>el.classList.add('faded'));
  document.addEventListener('mousemove',onMove);
  document.addEventListener('mouseup',onUp);
  document.addEventListener('touchmove',onMove,{passive:false});
  document.addEventListener('touchend',onUp);
}

function onMove(e){
  if(!drag.active) return;
  e.preventDefault();
  const cx=e.touches?e.touches[0].clientX:e.clientX;
  const cy=e.touches?e.touches[0].clientY:e.clientY;
  moveGhost(cx,cy);
  const rect=canvas.getBoundingClientRect();
  const mx=cx-rect.left, my=cy-rect.top;
  const room=G.rooms[G.curRoom];
  let found=null;
  room.def.zones.forEach(z=>{
    const r={x:z.rx*W(),y:z.ry*H(),w:z.rw*W(),h:z.rh*H()};
    if(mx>=r.x&&mx<=r.x+r.w&&my>=r.y&&my<=r.y+r.h) found=z.id;
  });
  if(found!==drag.overZone){drag.overZone=found;redraw();}
  if(found&&drag.item){
    const pts=calcScore(drag.item,found);
    const zl=room.def.zones.find(z=>z.id===found)?.label||found;
    showTip(drag.item.n,`${drag.item.h} • ${zl}`,pts,cx,cy);
  } else hideTip();
}

function onUp(){
  if(!drag.active) return;
  document.removeEventListener('mousemove',onMove); document.removeEventListener('mouseup',onUp);
  document.removeEventListener('touchmove',onMove); document.removeEventListener('touchend',onUp);
  ghost.style.display='none'; hideTip();
  document.querySelectorAll('.bitem.faded').forEach(el=>el.classList.remove('faded'));
  const zone=drag.overZone;
  if(drag.item&&zone){
    if(!drag.fromBox) removeItem(G.curRoom,drag.item.id);
    placeItem(G.curRoom,drag.item,zone);
  } else if(!drag.fromBox&&drag.item){
    const room=G.rooms[G.curRoom];
    if(!room.placed[drag.item.id]){
      const def=room.def.items.find(i=>i.id===drag.item.id);
      room.box.push({...def});
    }
    refreshBox(G.curRoom); redraw();
  }
  drag.active=false; drag.item=null; drag.overZone=null;
}

function moveGhost(cx,cy){ghost.style.left=cx+'px';ghost.style.top=cy+'px';}

// Canvas — pick up placed item
canvas.addEventListener('mousedown',e=>{
  if(drag.active) return;
  const rect=canvas.getBoundingClientRect();
  const mx=e.clientX-rect.left, my=e.clientY-rect.top;
  const room=G.rooms[G.curRoom];
  for(const item of Object.values(room.placed)){
    const r=zr(item.zone);
    if(!r) continue;
    const all=Object.values(room.placed).filter(i=>i.zone===item.zone);
    const idx=all.findIndex(i=>i.id===item.id);
    const n=all.length;
    const cols=Math.min(n,Math.max(1,Math.round(Math.sqrt(n*r.w/r.h))));
    const rows=Math.ceil(n/cols);
    const cw=r.w/cols, ch=r.h/rows;
    const col=idx%cols, row=Math.floor(idx/cols);
    const cx2=r.x+col*cw+cw/2, cy2=r.y+row*ch+ch/2;
    const size=Math.min(cw,ch)*0.44;
    if(Math.hypot(mx-cx2,my-cy2)<size+6){
      const def=room.def.items.find(i=>i.id===item.id);
      removeItem(G.curRoom,item.id);
      startDrag(e,{...def},false);
      return;
    }
  }
});

canvas.addEventListener('mousemove',e=>{
  if(drag.active) return;
  const rect=canvas.getBoundingClientRect();
  const mx=e.clientX-rect.left, my=e.clientY-rect.top;
  const room=G.rooms[G.curRoom];
  let onItem=false;
  for(const item of Object.values(room.placed)){
    const r=zr(item.zone);
    if(!r) continue;
    const all=Object.values(room.placed).filter(i=>i.zone===item.zone);
    const idx=all.findIndex(i=>i.id===item.id);
    const n=all.length;
    const cols=Math.min(n,Math.max(1,Math.round(Math.sqrt(n*r.w/r.h))));
    const rows=Math.ceil(n/cols);
    const cw=r.w/cols, ch=r.h/rows;
    const col=idx%cols, row=Math.floor(idx/cols);
    const cx2=r.x+col*cw+cw/2, cy2=r.y+row*ch+ch/2;
    const size=Math.min(cw,ch)*0.44;
    if(Math.hypot(mx-cx2,my-cy2)<size+6){
      onItem=true; canvas.style.cursor='grab';
      showTip(item.n,item.h,item.pts,e.clientX,e.clientY);
      break;
    }
  }
  if(!onItem){canvas.style.cursor='default';hideTip();}
});
canvas.addEventListener('mouseleave',hideTip);
canvas.addEventListener('touchstart',e=>{
  if(drag.active) return;
  const touch=e.touches[0];
  const rect=canvas.getBoundingClientRect();
  const mx=touch.clientX-rect.left, my=touch.clientY-rect.top;
  const room=G.rooms[G.curRoom];
  for(const item of Object.values(room.placed)){
    const r=zr(item.zone); if(!r) continue;
    const all=Object.values(room.placed).filter(i=>i.zone===item.zone);
    const idx=all.findIndex(i=>i.id===item.id), n=all.length;
    const cols=Math.min(n,Math.max(1,Math.round(Math.sqrt(n*r.w/r.h))));
    const cw=r.w/cols, ch=r.h/Math.ceil(n/cols);
    const col=idx%cols, row=Math.floor(idx/cols);
    const cx2=r.x+col*cw+cw/2, cy2=r.y+row*ch+ch/2;
    const size=Math.min(cw,ch)*0.44;
    if(Math.hypot(mx-cx2,my-cy2)<size+10){
      const def=room.def.items.find(i=>i.id===item.id);
      removeItem(G.curRoom,item.id);
      startDrag(e,{...def},false);
      return;
    }
  }
},{passive:false});

// ══════════════════════════════════════════════
//  UI HELPERS
// ══════════════════════════════════════════════
function renderPills(){
  const el=document.getElementById('pills'); el.innerHTML='';
  G.rooms.forEach((r,i)=>{
    const b=document.createElement('button');
    b.className='pill'+(i===G.curRoom?' active':'')+(r.unlocked?'':' locked');
    b.textContent=r.def.name;
    if(r.unlocked) b.onclick=()=>{G.curRoom=i;renderPills();refreshBox(i);redraw();};
    el.appendChild(b);
  });
}

function refreshBox(ri){
  if(ri!==G.curRoom) return;
  const room=G.rooms[ri];
  const bl=document.getElementById('box-list');
  const be=document.getElementById('box-done');
  bl.innerHTML='';
  document.getElementById('box-title').textContent=room.def.name;
  document.getElementById('box-cnt').textContent=`${room.box.length} ${room.box.length===1?'item':'itens'} restante${room.box.length===1?'':'s'}`;
  room.box.forEach(item=>{
    const d=document.createElement('div');
    d.className='bitem'; d.dataset.id=item.id;
    d.innerHTML=`<div class="bi-emoji">${item.e}</div><div class="bi-info"><div class="bi-name">${item.n}</div><div class="bi-sub">${item.h}</div></div><div class="bi-pts">+${item.bp}</div>`;
    d.addEventListener('mousedown',e=>startDrag(e,item,true));
    d.addEventListener('touchstart',e=>startDrag(e,item,true),{passive:false});
    bl.appendChild(d);
  });
  bl.style.display=room.box.length?'flex':'none';
  be.classList.toggle('vis',room.box.length===0);
}

function updateUI(){
  document.getElementById('score-val').textContent=G.score;
  const pct=Math.round(G.placed/G.total*100);
  document.getElementById('prog-fill').style.width=pct+'%';
  document.getElementById('prog-pct').textContent=pct+'%';
}

function setHint(ttl,msg){
  document.getElementById('hint-ttl').textContent=ttl;
  document.getElementById('hint-msg').textContent=msg;
}

function addLog(e,n,pts,perfect){
  const el=document.getElementById('log');
  const d=document.createElement('div');
  d.className='lrow'+(perfect?' perf':'');
  d.innerHTML=`<span class="le">${e}</span><span class="ln">${n}</span><span class="lp">+${pts}</span>`;
  el.insertBefore(d,el.firstChild);
  while(el.children.length>7) el.removeChild(el.lastChild);
}

let ntTimer=null;
function notify(msg){
  const el=document.getElementById('notif');
  el.textContent=msg; el.classList.add('on');
  clearTimeout(ntTimer); ntTimer=setTimeout(()=>el.classList.remove('on'),2200);
}

const tipEl=document.getElementById('tip');
function showTip(name,hint,pts,cx,cy){
  document.getElementById('tn').textContent=name;
  document.getElementById('th').textContent=hint;
  document.getElementById('tp').textContent=pts!=null?`+${pts} pts`:'';
  tipEl.style.left=(cx+14)+'px'; tipEl.style.top=(cy-10)+'px'; tipEl.style.display='block';
}
function hideTip(){tipEl.style.display='none';}

function spawnParticles(zone,ri,perfect){
  const r=zr(zone); if(!r) return;
  const rect=canvas.getBoundingClientRect();
  const sx=rect.left+r.x+r.w/2, sy=rect.top+r.y+r.h/2;
  const icons=perfect?['✨','⭐','💫','✨']:['👍','📦','✓','💛'];
  icons.forEach((ic,i)=>{
    const p=document.createElement('div'); p.className='particle'; p.textContent=ic;
    const a=(Math.random()*260-130)*Math.PI/180, d=40+Math.random()*60;
    p.style.cssText=`left:${sx}px;top:${sy}px;--px:${Math.cos(a)*d}px;--py:${Math.sin(a)*d-30}px;animation-delay:${i*55}ms;animation-duration:${700+i*80}ms`;
    document.body.appendChild(p); setTimeout(()=>p.remove(),1300+i*80);
  });
}

// ══════════════════════════════════════════════
//  RESTART
// ══════════════════════════════════════════════
document.getElementById('btn-restart').addEventListener('click',()=>{
  document.getElementById('victory').classList.remove('on');
  initGame(); renderPills(); refreshBox(0); updateUI(); redraw();
});

// ══════════════════════════════════════════════
//  BOOT
// ══════════════════════════════════════════════
initGame();
renderPills();
refreshBox(0);
updateUI();
resize();
</script>
</body>
</html>