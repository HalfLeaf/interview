module.exports = {
  lange: 'zh-CN',
  title: '进击的算法题',
  description: '进击的算法题',
  author: 'Half Leaf',
  port:8866,
  head: [
    ['link', { rel: 'icon', href: '/favicon.png' }],
    ['link', { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.css' }],
    ['link', { rel: "stylesheet", href: "https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/2.10.0/github-markdown.min.css" }]
  ],
  base: '/', // 这是部署到github相关的配置
  markdown: {
    lineNumbers: false, // 代码块显示行号
    config: md => {
      md.set({html: true})
      md.use(require("markdown-it-katex"))
    }
  },
  themeConfig: {
    nav:[ // 导航栏配置
      {text: 'Python', link: '/python/' },
      {text: 'Vue', link: '/vue/'},
      {text: 'MongoDB', link: '/mongodb/'},
      {text: '经典算法', link: '/algorithm/'},
      {text: 'Github', link: 'https://github.com/HalfLeaf/interview'},
      {text: '个人主页', link: 'http://halfleaf.github.io/'}  
    ],
    sidebar: 'auto', 
    sidebarDepth: 5, 
  },
  sidebar:[
    ['/', '首页'],
  ],
  evergreen: true,
  activeHeaderLinks: true,
  plugins: [
    ['@vuepress/plugin-back-to-top', true],
  ],
};