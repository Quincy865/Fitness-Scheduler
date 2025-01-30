
import { reportWebVitals } from 'web-vitals';

// Function to log results or send to an analytics endpoint
const reportMetrics = (metric) => {
  console.log(metric);
};

// Call the function to report web vitals
reportWebVitals(reportMetrics);
