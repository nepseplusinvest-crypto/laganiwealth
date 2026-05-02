let globalData = [];

fetch('data.json')
.then(r => r.json())
.then(d => {
  globalData = d.all;
  render("all", globalData);
  render("gainers", d.gainers);
  render("losers", d.losers);
});

function render(id, list){
  let html = "";
  list.forEach(s => {
    html += `
      <div class="stock">
        <span>${s.symbol}</span>
        <span class="${s.change >=0 ? 'green':'red'}">
          ${s.price} (${s.change}%)
        </span>
      </div>
    `;
  });
  document.getElementById(id).innerHTML = html;
}

document.getElementById("search").addEventListener("input", (e)=>{
  let val = e.target.value.toLowerCase();
  let filtered = globalData.filter(s =>
    s.symbol.toLowerCase().includes(val)
  );
  render("all", filtered);
});
