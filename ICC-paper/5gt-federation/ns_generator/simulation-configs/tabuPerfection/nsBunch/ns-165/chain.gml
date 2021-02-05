graph [
  node [
    id 0
    label 1
    disk 3
    cpu 2
    memory 1
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 1
    memory 5
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 3
    memory 3
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 6
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 4
    memory 12
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 4
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 76
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 166
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 154
  ]
  edge [
    source 0
    target 3
    delay 25
    bw 177
  ]
  edge [
    source 1
    target 5
    delay 29
    bw 190
  ]
  edge [
    source 2
    target 5
    delay 35
    bw 191
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 183
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 80
  ]
]
