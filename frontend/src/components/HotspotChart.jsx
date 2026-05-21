import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const COLORS = [
  "#16a34a",
  "#2563eb",
  "#ea580c",
  "#dc2626",
  "#7c3aed",
  "#0891b2",
];

export default function HotspotChart({ data }) {

  // only top 8 hotspots
  const filteredData = data.slice(0, 8);

  return (

    <div className="
      bg-white
      rounded-2xl
      shadow-lg
      p-6
      w-full
      h-[500px]
    ">

      <h2 className="text-2xl font-bold mb-6 text-gray-800">
        Emission Hotspots
      </h2>

      <div className="w-full h-[380px]">

        <ResponsiveContainer width="100%" height="100%">

          <PieChart>

            <Pie
              data={filteredData}
              dataKey="value"
              nameKey="name"
              cx="50%"
              cy="50%"
              outerRadius={120}
              label={false}
            >

              {filteredData.map((entry, index) => (

                <Cell
                  key={index}
                  fill={COLORS[index % COLORS.length]}
                />

              ))}

            </Pie>

            <Tooltip />

            <Legend />

          </PieChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}