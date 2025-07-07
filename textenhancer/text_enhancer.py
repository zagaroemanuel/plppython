import os
from pathlib import Path
import chardet
import textstat

def enhance_text(content):
    """Apply creative enhancements to text"""
    # Define creative transformations
    transformations = [
        lambda s: s.replace(" good ", " excellent "),
        lambda s: s.replace(" bad ", " suboptimal "),
        lambda s: s.replace(" important ", " crucial "),
        lambda s: s.replace(" big ", " substantial "),
        lambda s: s.replace(" small ", " compact "),
        lambda s: s.replace(" I ", " I, as an expert, "),
        lambda s: s.replace(" we ", " our team "),
        lambda s: s.replace(" you ", " valued client "),
        lambda s: s + "!" if not s.endswith(('.', '!', '?')) else s,
        lambda s: s[0].upper() + s[1:] if s else s
    ]
    
    # Apply all transformations
    enhanced = content
    for transform in transformations:
        enhanced = transform(enhanced)
    
    return enhanced

def process_file(input_file, output_file):
    """Process text file with creative enhancements"""
    try:
        input_path = Path(input_file).resolve()
        output_path = Path(output_file).resolve()
        
        print(f"\n📥 Input: {input_path}")
        print(f"📤 Output: {output_path}")
        
        # Create sample file if input doesn't exist
        if not input_path.exists():
            print("⚠️ Input file not found - creating sample file")
            sample_text = (
                "This is a sample text file.\n"
                "It shows how our text enhancement works.\n"
                "You'll notice important improvements!\n"
                "Good writing matters for clear communication."
            )
            input_path.write_text(sample_text, encoding='utf-8')
        
        # Read with encoding detection
        raw_data = input_path.read_bytes()
        encoding = chardet.detect(raw_data)['encoding'] or 'utf-8'
        
        # Handle UTF-16 specifically
        if raw_data[:2] == b'\xff\xfe':
            content = raw_data.decode('utf-16')
        else:
            content = raw_data.decode(encoding)
        
        # Analyze text statistics
        word_count = len(content.split())
        sentence_count = textstat.sentence_count(content)
        readability = textstat.flesch_reading_ease(content)
        
        print(f"\n📊 Text Analysis:")
        print(f"- Words: {word_count}")
        print(f"- Sentences: {sentence_count}")
        print(f"- Readability Score: {readability:.1f}/100")
        
        # Process content
        print("\n🎨 Enhancing text...")
        enhanced_lines = []
        for line in content.splitlines():
            if line.strip():
                enhanced = enhance_text(line)
                enhanced_lines.append(enhanced)
        
        # Write output
        output_content = "\n".join(enhanced_lines)
        output_path.write_text(output_content, encoding='utf-8')
        
        print(f"\n✅ Successfully created enhanced output!")
        print(f"🔍 Sample transformation:")
        
        # Show before/after comparison
        sample_input = content.splitlines()[0][:60] + "..." if content else ""
        sample_output = enhanced_lines[0][:60] + "..." if enhanced_lines else ""
        
        print(f"Original: {sample_input}")
        print(f"Enhanced: {sample_output}")
        
        return True

    except Exception as e:
        print(f"\n❌ Critical Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Setup paths
    base_dir = Path(__file__).parent
    input_file = base_dir / "input.txt"
    output_file = base_dir / "output.txt"
    
    print("="*50)
    print("✨ Creative Text Enhancement System")
    print("="*50)
    
    # Process files
    success = process_file(input_file, output_file)
    
    print("\n" + "="*50)
    print(f"Process {'completed successfully' if success else 'failed'}!")
    print("="*50)
