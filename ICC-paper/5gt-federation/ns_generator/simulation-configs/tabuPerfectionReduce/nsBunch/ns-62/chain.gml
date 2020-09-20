graph [
  node [
    id 0
    label 1
    disk 2
    cpu 3
    memory 3
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 2
    memory 13
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 1
    memory 8
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 4
    memory 12
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 3
    memory 15
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 4
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 166
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 57
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 52
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 152
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 181
  ]
  edge [
    source 3
    target 5
    delay 34
    bw 193
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 122
  ]
]
