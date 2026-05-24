import type {ReactNode} from 'react';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

interface FeatureItem {
  title: string;
  emoji: string;
  description: ReactNode;
  color: string;
  link: string;
}

const FeatureList: FeatureItem[] = [
  {
    title: 'Conexão',
    emoji: '🐕',
    color: '#FF6B6B',
    link: '/research-wiki/docs/conexao',
    description: (
      <>
        A revolução do vínculo humano-animal através de wearables inteligentes. 
        Comunicação interespecífica, pet tech e a nova economia do afeto.
      </>
    ),
  },
  {
    title: 'Segurança',
    emoji: '🛡️',
    color: '#4ECDC4',
    link: '/research-wiki/docs/seguranca',
    description: (
      <>
        Tecnologias de ponta para segurança pública e defesa. 
        K9 tech, smart cities, wearables táticos e vigilância inteligente.
      </>
    ),
  },
  {
    title: 'Confiança',
    emoji: '🤝',
    color: '#45B7D1',
    link: '/research-wiki/docs/confianca',
    description: (
      <>
        Acessibilidade e inclusão através da tecnologia. 
        Silver economy, health tech, assistência para idosos e PCDs.
      </>
    ),
  },
];

function Feature({title, emoji, description, color, link}: FeatureItem) {
  return (
    <div className="col col--4">
      <a href={link} className={styles.featureLink}>
        <div className={styles.featureCard} style={{'--feature-color': color} as React.CSSProperties}>
          <div className={styles.featureIcon} style={{backgroundColor: color + '15'}}>
            <span style={{fontSize: '3rem'}}>{emoji}</span>
          </div>
          <Heading as="h3" style={{color, marginTop: '1rem'}}>
            {title}
          </Heading>
          <p>{description}</p>
          <div className={styles.featureArrow} style={{color}}>
            Explorar →
          </div>
        </div>
      </a>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <Heading as="h2" className={styles.sectionTitle}>
            Três Pilares da Revolução
          </Heading>
          <p className={styles.sectionSubtitle}>
            Consciência, IA e Comunicação Interspecífica
          </p>
        </div>
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
