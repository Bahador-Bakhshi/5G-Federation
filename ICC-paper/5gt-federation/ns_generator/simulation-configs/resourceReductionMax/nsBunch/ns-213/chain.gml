graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 7
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 2
    memory 9
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 4
    memory 1
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 4
    memory 13
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 2
    memory 14
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 1
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 185
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 83
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 190
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 148
  ]
  edge [
    source 1
    target 4
    delay 33
    bw 183
  ]
  edge [
    source 2
    target 5
    delay 34
    bw 78
  ]
  edge [
    source 3
    target 5
    delay 26
    bw 85
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 156
  ]
]
