## Introduction

Some work is expensive: reading from a disk, querying a large database, calling a remote service, or computing a complicated result. If the same result is needed again and again, repeating the work is wasteful. A cache keeps a copy of the result in a place that is faster to reach, so later requests can be served quickly without redoing the work. Caching is one of the most effective ways of improving performance and reducing load, and one of the most common sources of subtle bugs, because a copy can differ from the original.

This topic explains what caches are, where they exist in a system, the strategies for filling and updating them, and the central difficulty of keeping cached data fresh.

**Definition:** A cache is a temporary store of copies of data or results, held in a location that is faster or cheaper to access than the original source, so that repeated requests can be served more quickly and with less load on the source.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_caching_basics.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A request arrow reaching a small fast box labelled Cache; a green Hit arrow returns immediately; a red Miss arrow continues to a large slow box labelled Source, and a copy path returns and stores into the cache.

ON-IMAGE TEXT: show a short bold title "Caching Basics" plus only these few labels, large and legible: Hit, Miss, Store. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Caching Works

Caching succeeds because of how access to data behaves in practice.

- **Temporal locality:** data used recently is likely to be used again soon.
- **Spatial locality:** data near the data just used is likely to be needed.
- **Skew:** a small fraction of the data accounts for most of the requests (often described by the 80/20 rule).
- **Repeated computation:** many results are requested far more often than they change.

The speed gap is large. Reading from memory is thousands of times faster than from a disk, and far faster than a request across a network.

## Key Terms

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The requested data is in the cache and is served from it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Miss</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">It is not in the cache, so it must be fetched from the source</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hit ratio</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The fraction of requests that are hits; the main measure of the value of a cache</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Eviction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Removal of entries to make room when the cache is full</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time to live (TTL)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How long an entry may be used before it expires</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invalidation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Removing or updating entries when the source changes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stale data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A cached copy that no longer matches the source</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Warm and cold cache</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A warm cache is already populated; a cold one is empty, as after a start</td>
    </tr>
  </tbody>
</table>

## Where Caches Exist

Caches appear at every level.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Processor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small, very fast memories close to the processor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Registers and levels of hardware cache</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operating system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Disk data kept in memory</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The page cache</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Application memory</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Values kept in memory inside the program itself</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Computed results, lookup tables</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Distributed cache</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A shared, in-memory store used by many application servers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redis, Memcached</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Database</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Query results and recently used data pages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The database buffer pool</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Web browser</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Files and responses stored on the device of the user</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Images, scripts, API responses</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Content delivery network (CDN)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Servers around the world that hold copies of content close to users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Static files, media, some pages</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reverse proxy or gateway</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A server in front of the application that stores responses</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whole-page and API response caching</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">DNS</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resolved addresses remembered for a time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Domain-name lookups</td>
    </tr>
  </tbody>
</table>

The closer a cache is to the user, the faster the response and the less load on everything behind it, but the harder it is to control or invalidate.

## Caching Strategies

How data enters and is updated in the cache defines the strategy.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strategy</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it works</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Advantages</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Disadvantages</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cache-aside (lazy loading)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The application checks the cache; on a miss it reads the source, stores the result in the cache, and returns it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple; only requested data is cached; cache failure is survivable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">First request is slow; data can become stale</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read-through</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The cache itself loads from the source on a miss</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Application code is simpler</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The cache needs to know how to load</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write-through</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every write goes to the cache and the source together</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cache is consistent with source</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slower writes; caches data that may never be read</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write-behind (write-back)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Writes go to the cache and are saved to the source later, in batches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Very fast writes; fewer source operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk of losing data if the cache fails before saving</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refresh-ahead</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Popular entries are refreshed before they expire</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoids slow misses for hot data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wasted work if the prediction is wrong</td>
    </tr>
  </tbody>
</table>

## Eviction Policies

A cache has limited space, so it must decide what to remove.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Policy</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rule</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Suited to</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">LRU (least recently used)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove the entry unused for the longest time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">General purpose; the most common</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">LFU (least frequently used)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove the entry used the fewest times</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stable popularity</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">FIFO (first in, first out)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove the oldest entry</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple cases</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">TTL expiry</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove after a fixed time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data that goes out of date predictably</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Random</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove any entry</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cheap and surprisingly adequate</td>
    </tr>
  </tbody>
</table>

## The Hard Part: Freshness

A famous saying, often attributed to Phil Karlton, holds that there are only two hard things in computer science: cache invalidation and naming things. Whenever the source changes, copies become wrong. Approaches include:

- **Expiry by time:** accept staleness up to the TTL. Simple, and suitable when slightly old data is acceptable.
- **Explicit invalidation:** remove or update the entry whenever the source changes. Accurate, but every code path that changes data must remember to do it.
- **Versioned keys:** include a version in the key, so that new data simply uses a new key and old entries age out.
- **Event-driven invalidation:** changes publish events that caches subscribe to.
- **Validation:** ask the source whether the copy is still valid, as HTTP does with version tags, saving the cost of transferring unchanged data.

The question to ask is: **how stale may this data be?** A menu description may be hours old; a stock count at checkout may not be minutes old; a bank balance after a transfer should not be old at all. Different data deserves different policies.

## Problems to Anticipate

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Mitigation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stale reads</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users see outdated data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Short TTLs, invalidation on change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cache stampede (thundering herd)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A popular entry expires and many requests all miss at once, overwhelming the source</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lock so only one request refreshes; stagger expiry times with random variation; refresh ahead</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cold start</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">After a restart or deployment the empty cache leaves the source to take the full load</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Warm the cache gradually; protect the source with rate limits</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cache penetration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requests for data that does not exist always miss and reach the source</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cache the absence of data for a short time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inconsistency across caches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Different servers or layers hold different versions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared cache, or tolerate and bound the difference</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Memory pressure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too much cached data crowds out other needs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Size limits and eviction policies</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Caching private data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The response meant for one user is served to another</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build keys carefully; mark personalised responses as not shareable</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hiding bugs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A cache can mask a slow query that should be fixed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fix the root cause; measure with and without the cache</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependency on the cache</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system fails if the cache is down</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design so that a cache failure reduces speed, not correctness</td>
    </tr>
  </tbody>
</table>

## When to Use a Cache

Caching adds complexity, so it should answer a measured need.

1. **Measure** first to find the real bottleneck.
2. **Optimise the source** where possible; a better index may remove the need.
3. **Cache data that is read often and changes rarely,** and is expensive to produce.
4. **Decide the acceptable staleness** and the invalidation method before building.
5. **Monitor** hit ratio, latency, and evictions, and confirm the cache is doing its job.
6. **Plan for loss:** the cache should be rebuildable, never the only copy.

## HTTP Caching

The web has its own built-in caching, controlled by headers on responses that say how long a response may be reused, whether shared caches such as CDNs may store it, and how to check whether it is still valid. Used well, it lets browsers and CDNs absorb a large share of traffic. Static files, images, and rarely changing API responses are good candidates; personalised or sensitive responses must be excluded.

<!--
IMAGE PROMPT  ->  generate as images/02_cache_layers_and_strategies.png   (16:9 explanatory diagram, place here)

Left: a vertical stack from User to Browser cache, CDN, Application cache, Database, each layer with a speed label (fast to slow). Right: cache-aside flow in four numbered steps (check cache, miss, read source, store and return), with a stale-data warning icon.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Cache with Care

1. A page's popular dish list takes a long time to build and changes once a day. Is it a good caching candidate, and what expiry would you choose?
2. A cached entry for the day's most popular item expires and the database is overwhelmed. What happened, and how can it be avoided?
3. Why should a cache never be the only copy of important data?

For case 1, yes, as it is read often, changes rarely, and is costly; an expiry of up to a day, or invalidation when the list is rebuilt. For case 2, a cache stampede; allow only one request to refresh, stagger expiry, or refresh ahead. For case 3, caches are temporary and can lose entries at any time, so the source of truth must be held elsewhere.

## Conclusion

A cache is a temporary store of copies of data or results, held in a location that is faster or cheaper to access than the original source, so that repeated requests can be served more quickly and with less load on the source. The strategies of filling, evicting, and invalidating, together with a clear decision about acceptable staleness, determine whether a cache is a benefit or a source of bugs.

Faster data access also means more requests are handled at the same time, which brings a new class of problems in application code. The final topic of this unit covers concurrency.
