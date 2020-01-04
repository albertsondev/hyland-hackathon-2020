document.addEventListener('DOMContentLoaded', () => {
  let navDrawer = document.getElementById('navigation-drawer');
  let navUnderlay = document.getElementById('navigation-underlay');
  
  let toggleHidden = element => element.classList.toggle('hidden');
  
  let navToggle = () => [navDrawer, navUnderlay].forEach(e => toggleHidden(e));
  
  document.getElementById('show-navigation').onclick = navToggle;
  navUnderlay.onclick = navToggle;
});
