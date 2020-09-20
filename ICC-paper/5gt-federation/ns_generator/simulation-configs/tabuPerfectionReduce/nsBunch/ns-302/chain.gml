graph [
  node [
    id 0
    label 1
    disk 5
    cpu 3
    memory 6
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 10
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 4
    memory 9
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 3
    memory 6
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 2
    memory 15
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 3
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 161
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 60
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 156
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 133
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 145
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 122
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 177
  ]
]
