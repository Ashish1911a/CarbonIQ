import { useEffect, useState } from "react";
import api from "./api";

export default function useAnalytics() {

  const [analytics, setAnalytics] = useState({
    yoy: [],
    hotspots: [],
    trends: [],
    intensity: {},
  });

  const [loading, setLoading] = useState(true);

  useEffect(() => {

    const fetchAnalytics = async () => {

      try {

        const [
          yoyRes,
          hotspotRes,
          intensityRes,
          trendsRes
        ] = await Promise.all([
          api.get("/analytics/yoy"),
          api.get("/analytics/hotspots"),
          api.get("/analytics/intensity"),
          api.get("/analytics/monthly-trends"),
        ]);

        console.log("YOY:", yoyRes.data);
        console.log("HOTSPOTS:", hotspotRes.data);
        console.log("INTENSITY:", intensityRes.data);
        console.log("TRENDS:", trendsRes.data);

        // YOY FORMAT
        const yoyData = Object.entries(yoyRes.data).map(
          ([year, values]) => ({
            year,
            scope1: values["Scope 1"] || 0,
            scope2: values["Scope 2"] || 0,
            scope3: values["Scope 3"] || 0,
          })
        );

        // HOTSPOT FORMAT
        const hotspotData = Object.entries(hotspotRes.data).map(
          ([name, value]) => ({
            name,
            value,
          })
        );

        // TRENDS FORMAT
        const trendsData = Object.entries(trendsRes.data || {}).map(
          ([month, value]) => ({
            month,
            emissions: value,
          })
        );

        // KPI VALUES
        const total =
          yoyData.reduce(
            (sum, item) =>
              sum +
              item.scope1 +
              item.scope2 +
              item.scope3,
            0
          );

        const scope1 =
          yoyData.reduce((sum, item) => sum + item.scope1, 0);

        const scope2 =
          yoyData.reduce((sum, item) => sum + item.scope2, 0);

        const scope3 =
          yoyData.reduce((sum, item) => sum + item.scope3, 0);

        setAnalytics({
          yoy: yoyData,
          hotspots: hotspotData,
          trends: trendsData,
          intensity: {
            intensity:
              intensityRes.data.intensity || 0,
            total,
            scope1,
            scope2,
            scope3,
          },
        });

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);

      }
    };

    fetchAnalytics();

  }, []);

  return {
    analytics,
    loading,
  };
}