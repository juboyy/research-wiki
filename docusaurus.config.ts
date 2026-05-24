import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'AMIAU Research Wiki',
  tagline: 'Consciência, IA, Animais, Comunicação, IoT e Wearables',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://juboyy.github.io',
  baseUrl: '/research-wiki/',

  organizationName: 'juboyy',
  projectName: 'research-wiki',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'warn',

  i18n: {
    defaultLocale: 'pt-BR',
    locales: ['pt-BR'],
    localeConfigs: {
      'pt-BR': {
        label: 'Português',
        htmlLang: 'pt-BR',
      },
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/juboyy/research-wiki/tree/main/',
          routeBasePath: 'docs',
          showLastUpdateTime: true,
          showLastUpdateAuthor: true,
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          editUrl: 'https://github.com/juboyy/research-wiki/tree/main/',
          blogTitle: 'Revista AMIAU',
          blogDescription: 'Artigos periódicos sobre IA, consciência, animais, IoT e wearables',
          postsPerPage: 10,
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/amiau-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'AMIAU Research Wiki',
      logo: {
        alt: 'AMIAU Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'mainSidebar',
          position: 'left',
          label: 'Wiki',
        },
        {
          to: '/blog',
          label: 'Revista',
          position: 'left',
        },
        {
          type: 'dropdown',
          label: 'Temas',
          position: 'left',
          items: [
            { to: '/docs/conexao', label: 'Conexão' },
            { to: '/docs/seguranca', label: 'Segurança' },
            { to: '/docs/confianca', label: 'Confiança' },
          ],
        },
        {
          href: 'https://github.com/juboyy/research-wiki',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Wiki',
          items: [
            { label: 'Introdução', to: '/docs/intro' },
            { label: 'Conexão', to: '/docs/conexao' },
            { label: 'Segurança', to: '/docs/seguranca' },
            { label: 'Confiança', to: '/docs/confianca' },
          ],
        },
        {
          title: 'Comunidade',
          items: [
            { label: 'GitHub', href: 'https://github.com/juboyy/research-wiki' },
            { label: 'Issues', href: 'https://github.com/juboyy/research-wiki/issues' },
          ],
        },
        {
          title: 'Sobre',
          items: [
            { label: 'AMIAU Project', href: '#' },
            { label: 'AutoResearchClaw', href: '#' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} AMIAU Project. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
