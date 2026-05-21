import Navbar from "../components/Navbar";
import KPI from "../components/KPI";
import IntensityCard from "../components/IntensityCard";
import YoYChart from "../components/YoYChart";
import HotspotChart from "../components/HotspotChart";
import TrendChart from "../components/TrendChart";
import UploadExcel from "../components/UploadExcel";

import { motion } from "framer-motion";

import useAnalytics from "../useAnalytics";

export default function Dashboard() {

  const { analytics, loading } = useAnalytics();

  console.log(analytics);

  if (loading) {

    return (

      <div className="
        min-h-screen
        flex
        items-center
        justify-center
        bg-gray-100
      ">

        <div className="
          text-2xl
          font-bold
          text-green-600
          animate-pulse
        ">
          Loading ESG Dashboard...
        </div>

      </div>
    );
  }

  return (

    <div className="
      min-h-screen
      bg-gradient-to-br
      from-gray-100
      via-white
      to-green-50
    ">

      <Navbar />

      <motion.div

        initial={{ opacity: 0, y: 20 }}

        animate={{ opacity: 1, y: 0 }}

        transition={{ duration: 0.5 }}

        className="
          px-4
          sm:px-6
          lg:px-8
          py-8
          max-w-[1800px]
          mx-auto
          space-y-8
        "
      >

        {/* HEADER */}

        <div className="space-y-2">

          <h2 className="
            text-3xl
            sm:text-4xl
            font-bold
            text-gray-800
          ">
            Sustainability Overview
          </h2>

          <p className="
            text-gray-500
            text-sm
            sm:text-base
          ">
            Enterprise ESG analytics and emissions monitoring dashboard
          </p>

        </div>

        {/* KPI SECTION */}

        <div className="
          grid
          grid-cols-1
          md:grid-cols-2
          lg:grid-cols-3
          2xl:grid-cols-5
          gap-6
        ">

          <KPI
            title="Total Emissions"
            value={analytics?.intensity?.total || 0}
            color="bg-gradient-to-br from-green-600 to-emerald-500"
          />

          <KPI
            title="Scope 1"
            value={analytics?.intensity?.scope1 || 0}
            color="bg-gradient-to-br from-blue-600 to-cyan-500"
          />

          <KPI
            title="Scope 2"
            value={analytics?.intensity?.scope2 || 0}
            color="bg-gradient-to-br from-orange-500 to-amber-400"
          />

          <KPI
            title="Scope 3"
            value={analytics?.intensity?.scope3 || 0}
            color="bg-gradient-to-br from-red-500 to-pink-500"
          />

          <IntensityCard
            value={analytics?.intensity?.intensity || 0}
          />

        </div>

        {/* CHART SECTION */}

        <div className="
          grid
          grid-cols-1
          2xl:grid-cols-2
          gap-8
          items-stretch
        ">

          <YoYChart
            data={analytics?.yoy || []}
          />

          <HotspotChart
            data={analytics?.hotspots || []}
          />

        </div>

        {/* TREND CHART */}

        <TrendChart
          data={analytics?.trends || []}
        />

        {/* UPLOAD SECTION */}

        {/* <div className="pt-2">

          <UploadExcel />

        </div> */}

      </motion.div>

    </div>
  );
}