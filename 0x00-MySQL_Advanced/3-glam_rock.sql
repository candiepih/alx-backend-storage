-- script that lists all bands with Glam rock as their
-- main style, ranked by their longevity
SELECT band_name, (COALESCE(split, 2021) - formed) as lifespan FROM 
metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
