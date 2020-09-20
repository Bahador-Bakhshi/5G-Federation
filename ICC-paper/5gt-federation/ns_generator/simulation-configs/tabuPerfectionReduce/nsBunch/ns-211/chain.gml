graph [
  node [
    id 0
    label 1
    disk 2
    cpu 4
    memory 16
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 4
    memory 1
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 1
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 2
    memory 4
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 1
    memory 7
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 2
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
    delay 35
    bw 104
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 183
  ]
  edge [
    source 0
    target 3
    delay 30
    bw 198
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 102
  ]
  edge [
    source 2
    target 5
    delay 26
    bw 160
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 102
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 161
  ]
]
