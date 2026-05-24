import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className={styles.heroBackground}>
        <div className={styles.heroGrid} />
      </div>
      <div className="container">
        <div className={styles.heroContent}>
          <div className={styles.heroBadge}>
            🧬 Revista Científica + Wiki Técnica
          </div>
          <Heading as="h1" className={styles.heroTitle}>
            {siteConfig.title}
          </Heading>
          <p className={styles.heroSubtitle}>{siteConfig.tagline}</p>
          <div className={styles.heroStats}>
            <div className={styles.statItem}>
              <span className={styles.statNumber}>3</span>
              <span className={styles.statLabel}>Pilares</span>
            </div>
            <div className={styles.statDivider} />
            <div className={styles.statItem}>
              <span className={styles.statNumber}>∞</span>
              <span className={styles.statLabel}>Possibilidades</span>
            </div>
            <div className={styles.statDivider} />
            <div className={styles.statItem}>
              <span className={styles.statNumber}>5K+</span>
              <span className={styles.statLabel}>Palavras/Artigo</span>
            </div>
          </div>
          <div className={styles.buttons}>
            <Link
              className={clsx('button button--lg', styles.buttonPrimary)}
              to="/docs/intro">
              📖 Explorar Wiki
            </Link>
            <Link
              className={clsx('button button--lg', styles.buttonSecondary)}
              to="/blog">
              📰 Ler Revista
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={siteConfig.title}
      description="Consciência, IA, Animais, Comunicação, IoT e Wearables - Pesquisa de ponta em português">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
        <section className={styles.ctaSection}>
          <div className="container">
            <div className={styles.ctaCard}>
              <Heading as="h2" className={styles.ctaTitle}>
                🔬 Pesquisa Automatizada
              </Heading>
              <p className={styles.ctaText}>
                Artigos gerados automaticamente a cada 4 horas via <strong>AutoResearchClaw</strong>.
                Qualidade paper, referências científicas, temas de mercado.
              </p>
              <div className={styles.ctaTags}>
                <span className={styles.ctaTag}>Consciência</span>
                <span className={styles.ctaTag}>IA</span>
                <span className={styles.ctaTag}>Animais</span>
                <span className={styles.ctaTag}>IoT</span>
                <span className={styles.ctaTag}>Wearables</span>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
