graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 16
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 4
    memory 6
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 3
    memory 7
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 1
    memory 8
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 4
    memory 14
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 3
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 81
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 155
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 189
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 190
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 156
  ]
  edge [
    source 3
    target 4
    delay 34
    bw 68
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 85
  ]
]
