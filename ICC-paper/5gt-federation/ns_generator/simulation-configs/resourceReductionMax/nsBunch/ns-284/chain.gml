graph [
  node [
    id 0
    label 1
    disk 4
    cpu 1
    memory 4
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 2
    memory 4
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 1
    memory 3
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 2
    memory 14
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 4
    memory 9
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 1
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 153
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 99
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 107
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 104
  ]
  edge [
    source 1
    target 4
    delay 35
    bw 81
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 134
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 183
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 178
  ]
]
