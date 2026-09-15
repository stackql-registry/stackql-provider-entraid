import {themes as prismThemes} from 'prism-react-renderer';
import { createConfig } from './.shared-config/index.js';
import { providerName, providerTitle } from './provider.js';

const config = createConfig({ providerName, providerTitle, prismThemes });

// URL form. Keep the Docusaurus default (pages emitted as <route>/index.html)
// regardless of the shared config's trailingSlash setting, so GitHub Pages
// serves both /services/x/y and /services/x/y/. A trailingSlash: false site
// emits <route>.html instead, which returns 404 for the trailing-slash URL.
delete config.trailingSlash;

export default config;
