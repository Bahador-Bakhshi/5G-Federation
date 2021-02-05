graph [
  node [
    id 0
    label 1
    disk 5
    cpu 2
    memory 13
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 3
    memory 6
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 2
    memory 15
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 12
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 3
    memory 9
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 2
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 54
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 183
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 57
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 127
  ]
  edge [
    source 1
    target 5
    delay 35
    bw 91
  ]
  edge [
    source 2
    target 4
    delay 30
    bw 146
  ]
  edge [
    source 3
    target 4
    delay 34
    bw 197
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 134
  ]
]
