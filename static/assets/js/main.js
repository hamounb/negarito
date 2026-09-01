
document.addEventListener("DOMContentLoaded", () => {
  const progress = document.createElement("div");
  progress.className = "scroll-progress";
  document.body.appendChild(progress);

  const onScroll = () => {
    const h = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + "%";
  };
  window.addEventListener("scroll", onScroll, {passive:true});
  onScroll();

  const obs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        entry.target.classList.add("is-visible");
        obs.unobserve(entry.target);
      }
    });
  }, {threshold:.12});
  document.querySelectorAll("[data-reveal],[data-mask]").forEach(el => obs.observe(el));

  document.querySelectorAll("[data-filter]").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("[data-filter]").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const f = btn.dataset.filter;
      document.querySelectorAll("[data-category]").forEach(card => {
        card.classList.toggle("is-hidden", !(f === "all" || card.dataset.category === f));
      });
    });
  });

  document.querySelectorAll("[data-blog-filter]").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("[data-blog-filter]").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const f = btn.dataset.blogFilter;
      document.querySelectorAll("[data-blog-category]").forEach(card => {
        card.classList.toggle("is-hidden", !(f === "all" || card.dataset.blogCategory === f));
      });
    });
  });

  const sections = document.querySelectorAll("[data-project-section]");
  const links = document.querySelectorAll(".project-index a");
  if(sections.length && links.length){
    const secObs = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if(entry.isIntersecting){
          links.forEach(a => a.classList.toggle("active", a.getAttribute("href") === "#" + entry.target.id));
        }
      });
    }, {rootMargin:"-35% 0px -55% 0px"});
    sections.forEach(s => secObs.observe(s));
  }

  const current = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-link").forEach(a => {
    if(a.getAttribute("href") === current) a.classList.add("active");
  });
});
