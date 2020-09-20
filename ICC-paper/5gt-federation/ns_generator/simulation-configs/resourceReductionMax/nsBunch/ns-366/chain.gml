graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 5
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 2
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 1
    memory 15
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 11
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 1
    memory 8
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 4
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 193
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 117
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 179
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 57
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 167
  ]
  edge [
    source 2
    target 5
    delay 28
    bw 163
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 116
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 193
  ]
]
