import "../styles/globals.css";
import { Provider } from "react-redux";
import store from "../store";
import "./style.css";
import { DefaultSeo } from "next-seo";
import Layout from "../components/layout/Layout";

function MyApp({ Component, pageProps }) {
  return (
    <Provider store={store}>
      <DefaultSeo
        title="owerri jobhunt"
        description="over 2000 jobs available for Grabs"
      />
      <Layout>
        <Component {...pageProps} />
      </Layout>
    </Provider>
  );
}

export default MyApp;
