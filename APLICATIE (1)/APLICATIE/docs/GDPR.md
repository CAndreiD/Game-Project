# GDPR & Data Privacy - Hangman 3D

## 1. Overview

Hangman 3D is a word-guessing game application with integrated data collection features. This document outlines how the application handles data, privacy compliance, and user information.

## 2. Data Collection Policy

### 2.1 Gameplay Data (Not Collected)

The core Hangman game does **NOT** collect or store:
- ❌ User identity information
- ❌ Game progress or scores
- ❌ Session data
- ❌ Cookies or tracking pixels
- ❌ Browser fingerprints

**Rationale:** Game state is managed in-memory and lost when browser closes.

### 2.2 External API Data (Collected)

The application includes a **Data Pipeline** feature that collects data from external APIs:

**Source:** JSONPlaceholder API (`https://jsonplaceholder.typicode.com`)

**Data Collected:**
- Post metadata (id, userId, title, body)
- User information (id, name, email, address, company info)
- Comments data (id, postId, name, email, body)

**Purpose:** 
- Demonstration of data collection capabilities
- Testing and development
- Educational purposes only

**Retention:** Data is processed and stored in:
- `output/*.csv` - CSV files (local storage only)
- `logs/*.log` - Application logs (local storage only)

**No transmission to third parties** - Data stays on the user's machine.

## 3. GDPR Compliance

### 3.1 Legal Basis

Since Hangman 3D processes minimal personal data and is designed as:
- A **non-commercial application**
- **Local-only processing** (no data transmission)
- **Educational purpose**

GDPR compliance is achieved through:

#### ✅ Data Minimization (Article 5)
- Only necessary data is collected
- External API data is demo-only (JSONPlaceholder)
- No user identification required

#### ✅ Purpose Limitation (Article 5)
- Data collected only for:
  - Demonstrating API integration capabilities
  - Educational testing
  - Local data processing pipeline

#### ✅ Storage Limitation (Article 5)
- CSV exports stored locally in `output/` directory
- Logs stored locally in `logs/` directory
- No cloud/remote storage
- Users can delete files anytime

#### ✅ Transparency (Articles 13-14)
- This privacy policy provides clear information
- Data processing is logged (see `logs/`)
- Users can inspect generated CSV files

### 3.2 User Rights

Users have the following rights:

**Right to Access (Article 15)**
- ✅ View generated CSV files in `output/` directory
- ✅ Inspect application logs in `logs/` directory

**Right to Deletion (Article 17)**
- ✅ Delete `output/*.csv` files
- ✅ Delete `logs/*.log` files
- Application provides no "undo" - once deleted, data is gone

**Right to Data Portability (Article 20)**
- ✅ CSV files are in open format (can be imported to other applications)
- ✅ Easy to export to other systems

**Right to Object (Article 21)**
- ✅ Users can disable data pipeline (don't call `/api/data/pipeline`)
- ✅ Core game works without data collection

### 3.3 Data Processing Activities

| Activity | Personal Data? | Legal Basis | Location |
|----------|---------------|-----------|-|----------|
| Game state | ❌ No | N/A | In-memory only |
| API data pipeline | ⚠️ Demo only | Legitimate interest | Local storage |
| Application logs | Minimal | System operation | `logs/` directory |

## 4. Data Controller Information

**Application Name:** Hangman 3D  
**Version:** 1.0.0  
**Type:** Open-source educational game  
**Repository:** GitHub (to be specified)  

**Data Processor:** Local machine (user's computer)

## 5. Implementation Details

### 5.1 No Tracking

The application includes **NO**:
- Analytics libraries (Google Analytics, Mixpanel, etc.)
- Advertisement tracking
- User identification systems
- Session tokens
- Account creation/login

### 5.2 Data Security

**At Rest:**
- CSV files stored in local `output/` directory
- Logs stored in local `logs/` directory
- No encryption required (local storage, user's machine)

**In Transit:**
- External API calls use HTTPS
- No sensitive data transmitted
- JSONPlaceholder API handles demo data

### 5.3 Third-Party Services

**External API Used:**
- **JSONPlaceholder** - Public test API
  - No user data
  - Public domain
  - No data sharing agreement needed
  - Used for demo/educational purposes

**No other third-party data processors**

## 6. Data Retention

- **CSV files:** Until manually deleted by user
- **Log files:** Until manually deleted by user
- **Game sessions:** Lost on browser close (in-memory only)
- **Recommended retention:** Delete after testing/learning

## 7. Special Categories of Data

**Not processed by Hangman 3D:**
- ❌ Race or ethnicity
- ❌ Political opinions
- ❌ Religious beliefs
- ❌ Health data
- ❌ Biometric data
- ❌ Genetic data
- ❌ Criminal records

## 8. Data Breach Response

In case of unauthorized access to local files:

1. Delete `output/` directory contents
2. Delete `logs/` directory contents
3. Reinstall application from clean source

No breach notification required as no centralized data storage exists.

## 9. International Transfers

**Data does NOT leave your machine** - No international transfers occur.

## 10. Contact & Questions

For questions about data privacy in Hangman 3D:
- Review source code (open-source on GitHub)
- Check `src/hangman_3d/` modules for data handling
- Inspect logs and CSV files generated by the application

## 11. Changelog

| Date | Change |
|------|--------|
| 2025-12-22 | Initial GDPR documentation |

---

**Last Updated:** 2025-12-22  
**Hangman 3D Version:** 1.0.0  
**Status:** Compliant with GDPR for educational use
